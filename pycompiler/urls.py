from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="indexpage"),
    path('runcode', views.runcode, name="runcode"),
]

# from pycompiler.views import CompileCodeView
#
# urlpatterns = [
#     path('compile', CompileCodeView.as_view(), name='CompileCodeView')
# ]