from rest_framework import serializers
from groups.models import ShoppingGroup
from users.api.serializers import UserDetailSerializer


class ShoppingGroupCreateSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=10, allow_null=False, allow_blank=False, write_only=True)
    owner = UserDetailSerializer(read_only=True)

    class Meta:
        model = ShoppingGroup
        fields = ('name', 'password', 'owner')

    def create(self, validated_data):
        user = self.context['request'].user
        shopping_group = ShoppingGroup(owner=user, name=validated_data["name"])
        shopping_group.password = validated_data['password']
        shopping_group.save()
        shopping_group.members.add(user)
        shopping_group.save()
        return shopping_group

    def validate_name(self, value):
        qs = ShoppingGroup.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("Group with this name exists!")
        else:
            return value


class ShoppingGroupUpdateDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(max_length=10, allow_null=False, allow_blank=False, write_only=True, required=False)
    owner = UserDetailSerializer(read_only=True)

    class Meta:
        model = ShoppingGroup
        fields = ('name', 'password', 'owner')

    def update(self, instance, validated_data):
        shopping_group = instance
        print('xD')
        if "name" in validated_data:
            shopping_group.name = validated_data["name"]
        if "password" in validated_data:
            shopping_group.password = validated_data["password"]
        shopping_group.save()
        return shopping_group

    def validate_name(self, value):
        qs = ShoppingGroup.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("This name has used.")
        else:
            return value
