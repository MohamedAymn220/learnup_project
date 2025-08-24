from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("courses/", views.all_courses, name="all_courses"),
    path("courses/add/", views.add_course, name="add_course"),
    path("courses/<int:course_id>/edit/", views.edit_course, name="edit_course"),
    path("courses/<int:course_id>/delete/", views.delete_course, name="delete_course"),
    path("course/<int:course_id>/", views.view_course, name="view_course"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
