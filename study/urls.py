from django.urls import path

from . import views

app_name = "study"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("cadastro/", views.signup_view, name="signup"),
    path("sair/", views.logout_view, name="logout"),
    path("", views.dashboard, name="dashboard"),
    path("estudar/", views.study_card, name="study"),
    path("responder/<int:segment_id>/", views.answer_card, name="answer"),
    path("ler/", views.read_learned, name="read"),
]
