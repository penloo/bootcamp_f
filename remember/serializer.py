from rest_framework import serializers
from .models import USER,CARD,HAS_RELATION

class CardSerializer(serializers.ModelSerializer):
# 모델을 JSON 형태로 변환
    class Meta:
        model = CARD # 모델 설정
        card_name = serializers.CharField()
        card_email = serializers.EmailField()
        card_info = serializers.CharField()
        card_photo = serializers.CharField()
        created_at = serializers.DateTimeField()
        update_at = serializers.DateTimeField(allow_null=True)

class UserSerializer(serializers.Serializer):

    class Meta:
        model = USER
        user_name = serializers.CharField()
        user_email = serializers.EmailField()
        password = serializers.CharField()
        phone_num = serializers.CharField()
        user_photo = serializers.CharField()
        is_user = serializers.BooleanField()
        created_at = serializers.DateTimeField()
        update_at = serializers.DateTimeField(allow_null=True)
        delete_at = serializers.DateTimeField(allow_null=True)
class RelationshipSerializer(serializers.Serializer):

     class Meta:
        model = HAS_RELATION
        relation_name = serializers.CharField()
        memo = serializers.CharField()
        created_at = serializers.DateTimeField()
        card_id = serializers.CharField(source='card.id')
        card_name = serializers.CharField(source='card.card_name')
        user_photo = serializers.CharField(source='card.user_photo')

        # fields = '__all__' # 모든 값