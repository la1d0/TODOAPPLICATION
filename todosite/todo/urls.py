from django.urls import path
from . import views


urlpatterns = [
    path('', views.TodoHome.as_view(), name='home'),
    path('task/<int:pk>/toogle/', views.ToogleTaskStatus.as_view(), name='toogletask'),
    path('task/<int:pk>/delete/', views.DeleteTask.as_view(), name='deletetask'),
    path('addpage/', views.AddPage.as_view(), name='addpage'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact')
]
