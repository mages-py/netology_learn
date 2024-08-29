from django.contrib.auth.models import User
from rest_framework import serializers, permissions

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        request = self.context["request"]

        if data.get('status','OPEN') == 'OPEN':
            if (request.method == 'POST' and Advertisement.objects.filter(creator=request.user, status='OPEN').count() >= 10) or \
                (request.method == 'PATCH' and Advertisement.objects.filter(creator=request.user, status='OPEN').exclude(id=request.parser_context['kwargs']['pk']).count() >= 10):
                
                raise serializers.ValidationError("Количество открытых объявлений не может быть больше 10")
        
        return data
