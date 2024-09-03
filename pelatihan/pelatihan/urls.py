"""
URL configuration for pelatihan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_views
from training import views as training_views
from user_training import views as user_training_views
from training_scores import views as training_scores_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.RegisterView.as_view(), name='register'),
    path('login/', user_views.LoginView.as_view(), name='login'),
    path('profile/', user_views.ProfileView.as_view(), name='profile'),
    path('trainings/', training_views.TrainingListCreateView.as_view(), name='training-list-create'),
    path('trainings/<int:pk>/', training_views.TrainingRetrieveUpdateDestroyView.as_view(), name='training-detail'),
    path('userTrainings/', user_training_views.UserTrainingListView.as_view(), name='user-training-list'),
    path('userTrainings/<int:pk>/', user_training_views.UserTrainingDetailView.as_view(), name='user-training-detail'),
    path('trainingScores/', training_scores_views.TrainingScoreListView.as_view(), name='training-score-list'),
    
]

