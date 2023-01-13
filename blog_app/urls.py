from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('detail_post/<int:id>', views.detail_post, name="detail_post"),
    path('logout', views.logout, name="logout"),
    path('mypost', views.mypost, name="mypost"),
    path('createpost', views.createpost, name="createpost"),
    path('edit/<int:id>', views.edit, name = 'edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]