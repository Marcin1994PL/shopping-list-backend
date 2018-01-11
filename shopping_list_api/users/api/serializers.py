from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models import Q


class UserCreateSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=150, allow_null=False, allow_blank=False)
    password = serializers.CharField(allow_null=False, allow_blank=False, write_only=True)
    email = serializers.CharField(allow_null=False, allow_blank=False)
    first_name = serializers.CharField(max_length=30, allow_null=False, allow_blank=False, required=False)
    last_name = serializers.CharField(max_length=30, allow_null=False, allow_blank=False, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.is_staff = True
        user.is_active = True
        if validated_data["first_name"] is not None:
            user.first_name = validated_data["first_name"]
        if validated_data["last_name"] is not None:
            user.last_name = validated_data["last_name"]
        user.save()
        token = Token.objects.create(user=user)
        token.save()
        return user

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This username has already by used")
        else:
            return value

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This email has already used.")
        else:
            return value


class UserLoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        required=False,
        allow_blank=True,
        write_only=True,
    )

    email = serializers.EmailField(
        required=False,
        allow_blank=True,
        write_only=True,
        label="Email Address"
    )

    token = serializers.CharField(
        allow_blank=True,
        read_only=True
    )

    password = serializers.CharField(
        required=True,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta(object):
        model = User
        fields = ['email', 'username', 'password', 'token']

    def validate(self, data):
        email = data.get('email', None)
        username = data.get('username', None)
        password = data.get('password', None)

        if not email and not username:
            raise serializers.ValidationError("Please enter username or email to login.")

        user = User.objects.filter(
            Q(email=email) | Q(username=username)
        ).exclude(
            email__isnull=True
        ).exclude(
            email__iexact=''
        ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError("Invalid credentials.")

        token, created = Token.objects.get_or_create(user=user_obj)
        data['token'] = token
        return data


class UserDetailSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, allow_null=False, allow_blank=False)
    email = serializers.CharField(allow_null=False, allow_blank=False)
    first_name = serializers.CharField(max_length=30, allow_null=False, allow_blank=False, required=False)
    last_name = serializers.CharField(max_length=30, allow_null=False, allow_blank=False, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, allow_null=False, allow_blank=False, required=False)
    email = serializers.CharField(allow_null=False, allow_blank=False, required=False)
    first_name = serializers.CharField(max_length=30, allow_null=False, allow_blank=False, required=False)
    last_name = serializers.CharField(max_length=30, allow_null=False, allow_blank=False, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        user = instance
        # if validated_data['username'] is not None:
        #     user.username = validated_data["username"]
        if "email" in validated_data:
            user.email = validated_data["email"]
        if "first_name" in validated_data:
            user.first_name = validated_data["first_name"]
        # if validated_data["last_name"] is not None:
        #     user.last_name = validated_data["last_name"]
        user.save()
        return user

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This username has already by used")
        else:
            return value

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This email has already used.")
        else:
            return value