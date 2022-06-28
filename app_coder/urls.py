from django.urls import path

from app_coder import views

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    path('about_us', views.about_us, name='about-us'),
    path('error', views.error, name='error'),
    path('search', views.search, name='Search'),
    path('pages', views.BlogListView.as_view(), name='blog-list'),
    path('pages/add/', views.BlogCreateView.as_view(), name='blog-add'),
    path('pages/<int:pk>/detail', views.BlogDetailView.as_view(), name='blog-detail'),
    path('pages/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('pages/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('login', views.login_request, name='user-login'),
    path('logout', views.logout_request, name='user-logout'),
    path('register', views.register, name='user-register'),
    path('register/update', views.user_update, name='user-update'),
    path('avatar/load', views.avatar_load, name='avatar-load'),
    path('accounts', views.ProfileListView.as_view(), name='profile-list'),
    path('accounts/add/', views.ProfileCreateView.as_view(), name='profile-add'),
    path('accounts/<int:pk>/detail', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('accounts/<int:pk>/update', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('accounts/<int:pk>/delete', views.ProfileDeleteView.as_view(), name='profile-delete'),
    path('profile/load', views.profile_load, name='profile-load'),
    path('blog/load', views.blog_load, name='blog-load'),
]
