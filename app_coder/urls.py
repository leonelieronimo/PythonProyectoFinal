from django.urls import path

from app_coder import views

app_name='app_coder'
urlpatterns = [
    path('', views.index, name='Home'),
    path('about_us', views.about_us, name='about-us'),
    path('error', views.error, name='error'),
    path('profesors', views.profesors, name='Profesors'),
    path('students', views.students, name='Students'),
    path('homeworks', views.homeworks, name='Homeworks'),
    path('formHTML', views.form_hmtl),
    path('course-django-forms', views.course_forms_django, name='CourseDjangoForms'),
    path('profesor/add', views.profesor_forms_django, name='profesor-add'),
    path('profesor/<int:pk>/update', views.update_profesor, name='profesor-update'),
    path('profesor/<int:pk>/delete', views.delete_profesor, name='profesor-delete'),
    path('homework/add', views.homework_forms_django, name='homework-add'),
    path('search', views.search, name='Search'),
    


    # Dajngo documentation -->  https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
    # Confirmo la url de la documentación es correcta, deben hacer scroll hasta esta parte:
    #
    # from django.urls import path
    # from myapp.views import AuthorCreateView, AuthorDeleteView, AuthorUpdateView

    # urlpatterns = [
    #     # ...
    #     path('author/add/', AuthorCreateView.as_view(), name='author-add'),
    #     path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    #     path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
    # ]
    #
    # Acá se ve la forma clara cómo Django realiza de forma stándar los nombres para urls, views y name del path.
    path('pages', views.BlogListView.as_view(), name='blog-list'),
    path('pages/add/', views.BlogCreateView.as_view(), name='blog-add'),
    path('pages/<int:pk>/detail', views.BlogDetailView.as_view(), name='blog-detail'),
    path('pages/<int:pk>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('pages/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('courses', views.CourseListView.as_view(), name='course-list'),
    path('course/add/', views.CourseCreateView.as_view(), name='course-add'),
    path('course/<int:pk>/detail', views.CourseDetailView.as_view(), name='course-detail'),
    path('course/<int:pk>/update', views.CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course-delete'),
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
