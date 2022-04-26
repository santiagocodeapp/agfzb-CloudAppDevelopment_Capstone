from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

# app_name = 'djangoapp'

urlpatterns = [

    # path(route='', view=views.get_dealerships, name='index'),
    # path(route='about/', view=views.about, name='about'),
    # path(route='contact/', view=views.contact, name='contact'),
    # path(route='login/', view=views.login_request, name='login'),
    # path(route='logout/', view=views.logout_request, name='logout'),
    # path(route='register/', view=views.registration_request, name='register'),

    path("", views.index, name = "index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("team/<str:team>", views.team, name="team"),
    path("send/report", views.send_report, name="send-report"),
    path("add/player", views.add_player, name="add-player"),
    path("add/team", views.add_team, name="add-team"),

  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)