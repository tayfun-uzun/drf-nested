from django.urls import path
from opak.modmain.views import ldene, userView
# from django.contrib import admin

urlpatterns = [
    # path('', ldene.as_view()),
    path('', userView.as_view()),
]