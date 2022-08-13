from django.urls import path
from .views import PetList, PetDetail, PetCreate, PetUpdate, PetDelete


urlpatterns = [
    # path('', views.home_page, name="home_page")
    path('pet-list', PetList.as_view(), name='pet_list'),
    path('pet/<int:pk>/', PetDetail.as_view(), name='pet_detail'),
    path('pet-create/', PetCreate.as_view(), name='pet_create'),
    path('pet-update/<int:pk>/', PetUpdate.as_view(), name='pet_update'),
    path('pet-delete/<int:pk>/', PetDelete.as_view(), name='pet_delete'),

]
