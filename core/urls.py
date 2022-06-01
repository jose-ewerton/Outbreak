
from django.urls import path
from .views import HomeView, LoginView, RegisterView, ProfileView, CreateNarrative, ListNarrative, DetailNarrative, UpdateView, DeleteNarrative, FeedView

urlpatterns = [
    #common pages 
    path('', HomeView.as_view(), name = 'home'),
    path('login/', LoginView.as_view(), name = 'login' ),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('feed/', FeedView.as_view(), name = 'feed'),
    path('profile', ProfileView.as_view(), name = 'profile' ),
    # CRUD pages
    path('create-narrative/', CreateNarrative.as_view(), name = 'create-narrative' ),
    path('update-narrative/:<int:pk>', UpdateView.as_view(), name = 'update-narrative'),
    path('detail-narrative/<int:pk>/', DetailNarrative.as_view(), name = 'detail-narrative'),
    path('list-narrative/', ListNarrative.as_view(), name = 'list-narrative'),
    path('delete-narrativa/:<int:pk>', DeleteNarrative.as_view(), name = 'delete-narrative'),
]
