from django.conf.urls import include
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from .views import RelationshipListAPIView,RelationshipDetailAPIView
from remember import views

# router = routers.DefaultRouter()
# router.register('api/v1/cards/add', views.post_card)
# router.register('users', fdislaf;d)
# router.register('refdjsafd', fdislaf;d)

urlpatterns = [
    path('api/v1/relations/all', RelationshipListAPIView.as_view(), name='relation-list-all'),
    path('api/v1/relations/detail/<str:card_id>/', RelationshipDetailAPIView.as_view(), name='relation-detail'),
    path('api/v1/cards/add',views.post_card),
    # path('api/v1/users/add',views.post_user),
]