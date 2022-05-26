
from django.urls import path
from .views import HomeView, LoginView, RegisterView, FeedView, CreateNarrative, ListNarrative, DetailNarrative

urlpatterns = [
    #common pages 
    path('', HomeView.as_view(), name = 'home'),
    path('login/', LoginView.as_view(), name = 'login' ),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('feed', FeedView.as_view(), name = 'feed' ),
    # CRUD pages
    path('create-narrative/', CreateNarrative.as_view(), name = 'create-narrative' ),
    path('list-narrative/', ListNarrative.as_view(), name = 'list-narrative' ),
    path('detail-narrative/<int:pk>/', DetailNarrative.as_view(), name = 'detail-narrative'),
    path('edit-narrativa/:<int:pk>',  ),
    path('delete-narrativa/:<int:pk>', ),
]
