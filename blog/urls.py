from django.urls import path
from .views import home,about,contact,dashboard,user_login,user_logout,user_signup,add_post,update_post,delete_post

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('blog.urls')),
    path('', home),
    path('about/', about,name='about'),
    path('contact/', contact,name='contact'),
    path('dashboard/',dashboard,name='dashboard'),
    path('user_signup/',user_signup,name='signup'),
    path('user_login/', user_login,name='login'),
    path('user_logout/',user_logout,name='logout'),
    path('addpost/', add_post,name='addpost'),
    path('updatepost/<int:id>', update_post,name='updatepost'),
    path('deletepost/<int:id>', delete_post,name='deletepost'),
]