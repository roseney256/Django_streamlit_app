"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include


from personal.views import (
    home_screen_views,
    landing_screen_views,
    dashboard_screen_views,
    highres_views,
    about_views,
)

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,

)

from machine.views import (
    predict_view,
    Table,
    upload_csv,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_screen_views, name="landing"),
    path('dashboard', dashboard_screen_views, name="dashboard"),
    path('home/', home_screen_views, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
    path('result/', predict_view, name="result"),
    path('table/', Table, name="table"),
    path('highres/', highres_views, name="highres"),
    path('upload/', upload_csv, name="upload"),
    path('about/', about_views, name="about"),
    
]
