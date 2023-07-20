from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django_neomodel import DjangoNode
from .serializer import  UserSerializer, CardSerializer, RelationshipSerializer
from .models import USER, CARD, HAS_RELATION

# @api_view(['POST'])
# class CardName(APIView):
#     def post(self, request):
#         newCard = CARD(card_name=request.data.card_name).save()
#         newCard.card_email = request.data.card_email
#         newCard.card_intro = request.data.card_intro
#         newCard.card_photo = request.data.card_photh
#         newCard.save()
        
#         return JsonResponse({"asd": "dfs"})


# class CardViewSet(viewsets.ModelViewSet):
#     queryset = CARD.nodes.all()
#     serializer_class = CardSerializer


class RelationshipListAPIView(generics.ListAPIView):
    serializer_class = RelationshipSerializer

    def get_queryset(self):
        phone_num = self.request.GET.get('phone_num')
        user = USER.nodes.filter(phone_num=phone_num).first()
        if not user:
            return HAS_RELATION.nodes.none()
        return user.relationships.all()

class RelationshipDetailAPIView(generics.RetrieveAPIView):
    queryset = HAS_RELATION.nodes.all()
    serializer_class = RelationshipSerializer
    lookup_field = 'card_id'
    lookup_url_kwarg = 'card_id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = {
            'message': '명함 상세정보 로드 성공',
            **serializer.data
        }
        return JsonResponse(data)


@api_view(['POST'])
def post_card(request):
    newCard = CARD().save()

    newCard.card_name = request.data["card_name"]
    newCard.card_email = request.data["card_email"]
    newCard.card_intro = request.data["card_intro"]
    newCard.card_photo = request.data["card_photo"]


    newCard.save()
    return JsonResponse({"card_name": newCard.card_name})
    return JsonResponse({"card_email": newCard.card_email})
    return JsonResponse({"card_intro": newCard.card_intro})
    return JsonResponse({"card_photo": newCard.card_photo})



# @api_view(['POST'])
# def post_user(request):
#     newUser = USER().save()
#
#     newUser.user_name = request.data["user_name"]
#     newUser.user_email = request.data["user_email"]
#     newUser.is_user = request.data["is_user"]
#
#     newUser.save()
#     return JsonResponse({"user_name": newUser.user_name})

    {
        "card_email": "aaaagaaa@naver.com",
        "card_intro": "intro",
        "card_photo": "photo",
        "card_name": "민지"
    }

    {
        "user_email": "aaaagaaa@naver.com",
        "is_user": "intro",
        "user_name": "민지"
    }