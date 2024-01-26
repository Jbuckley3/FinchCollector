from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),  
    path('finches/<int:pk>/', views.FinchDetailView.as_view(), name='finch_detail'),
    path('finches/create/', views.FinchCreateView.as_view(), name='finch_create'),
    path('finches/<int:pk>/update/', views.FinchUpdateView.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete/', views.FinchDeleteView.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_finch_feeding, name='add_feeding'),
    path('toys/', views.ToyList.as_view(), name='toy_list'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy_delete'),
]
