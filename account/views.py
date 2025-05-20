from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import CustomUser, OTPVerification
from .serializers import CustomUserSerializer, OTPRequestSerializer, OTPVerifySerializer
from .utils import generate_otp, send_otp_email
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def request_otp(request):
    serializer = OTPRequestSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        purpose = serializer.validated_data['purpose']

        user = None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            if purpose == 'password_reset':
                return Response({'error': 'User with this email does not exist'}, status=400)
            # For registration, user may not exist yet - create inactive user
            if purpose == 'registration':
                user = User.objects.create(
                    email=email,
                    is_active=False,
                )
                user.set_unusable_password()  # Prevent login before password set
                user.save()

        # Generate and save OTP
        otp_code = generate_otp()
        OTPVerification.objects.create(user=user, code=otp_code, purpose=purpose)

        # Send OTP email
        send_otp_email(email, otp_code, purpose)

        return Response({'message': f'OTP sent to {email}'})

    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp(request):
    serializer = OTPVerifySerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=400)

        try:
            otp_obj = OTPVerification.objects.get(
                user=user,
                code=code,
                is_used=False,
            )
        except OTPVerification.DoesNotExist:
            return Response({'error': 'Invalid OTP'}, status=400)

        if otp_obj.is_expired():
            return Response({'error': 'OTP expired'}, status=400)

        otp_obj.is_used = True
        otp_obj.save()

        # You can add logic to allow password reset here or
        # just respond with success, and frontend proceeds.

        return Response({'message': 'OTP verified successfully'})

    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([AllowAny])
def complete_signup(request):
    # Expect email, code (OTP), name, password in request.data
    email = request.data.get('email')
    code = request.data.get('code')
    name = request.data.get('name')
    password = request.data.get('password')

    if not all([email, code, name, password]):
        return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
        # Prevent duplicate signup if user already active
        if user.is_active:
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist. Please request OTP first.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        otp_obj = OTPVerification.objects.get(user=user, code=code, purpose='registration', is_used=False)
    except OTPVerification.DoesNotExist:
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)

    if otp_obj.is_expired():
        return Response({'error': 'OTP expired'}, status=status.HTTP_400_BAD_REQUEST)

    # Mark OTP as used
    otp_obj.is_used = True
    otp_obj.save()

    # Update user details and set password
    user.name = name
    user.set_password(password)
    user.is_active = True  # Just in case
    user.save()

    serializer = CustomUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)
    if user:
        login(request, user)
        serializer = CustomUserSerializer(user, context={'request': request})
        return Response(serializer.data)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_view(request):
    serializer = CustomUserSerializer(request.user, context={'request': request})
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def account_edit(request):
    # Use MultiPartParser to handle file uploads
    parser_classes = [MultiPartParser, FormParser]  # Allow file upload parsing
    
    # Serialize the user instance
    serializer = CustomUserSerializer(request.user, data=request.data, partial=True, context={'request': request})

    if serializer.is_valid():
        serializer.save()  # Save the user with updated data
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset(request):
    email = request.data.get('email')
    new_password = request.data.get('password')

    if not email or not new_password:
        return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    user.set_password(new_password)
    user.save()

    return Response({'message': 'Password reset successful.'})

