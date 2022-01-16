from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="indexpage"),
    path('runcode', views.runcode, name="runcode"),
    path('python/', views.api_python, name='api_python'),
]

# from pycompiler.views import CompileCodeView
#
# urlpatterns = [
#     path('compile', CompileCodeView.as_view(), name='CompileCodeView')
# ]