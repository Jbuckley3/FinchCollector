from django.urls import path
from . import views

from .views import FinchCreateView, FinchUpdateView, FinchDeleteView


urlpatterns = [
    path('', views.finches_index, name='index'),  # Change 'home' to 'finches_index'
    path('about/', views.about, name='about'),
    path('finches/', views.all_finches, name='index'),  # Update the name to 'all_finches'
    path('finches/<int:finch_id>/', views.finch_detail, name='finch_detail'),
    path('finch/add/', FinchCreateView.as_view(), name='finch_create'),
    path('finch/<int:pk>/edit/', FinchUpdateView.as_view(), name='finch_edit'),
    path('finch/<int:pk>/delete/', FinchDeleteView.as_view(), name='finch_delete'),
    path('finches/', views.finches_index, name='index')
]

