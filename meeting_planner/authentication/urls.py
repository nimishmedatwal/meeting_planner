from django.contrib import admin
from django.urls import path,include
from authentication import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('authentication.urls')),
    # path('welcome',welcome, name='welcome'),
    # path('date.html',date),
    # path('aboutme',AboutMe),
    # path('meeting/<int:id>',detail, name="detail"),
    # path('rooms',rooms_list, name="rooms"),
    # path('new',new,name="new"),
    path('',views.home,name="home"),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
]