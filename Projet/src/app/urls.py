from django.contrib.auth import views
from django.urls import path

from .views import Produit, ProductCreate, ProductUpdate, table, deleteProduct, register, connexion, deconnection,register

urlpatterns = [

    path('produit/', Produit, name="produit"),
    path('create/', ProductCreate, name="create"),
    path('update/<int:my_id>', ProductUpdate, name="update"),
    path('mamager', table, name='table'),
    path('delete/<int:my_id>', deleteProduct, name='delete'),
    path('register/', register, name='register'),
    path('login', connexion, name='login'),
    path('logout', deconnection, name='logout'),


    path('reset_password', views.PasswordResetView.as_view(template_name='app/password_reset.html'),
         name='reset_password'),
    path('reset_password_send', views.PasswordResetDoneView.as_view(template_name="app/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name="app/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete',
         views.PasswordResetCompleteView.as_view(template_name="app/password_reset_done.html"),
         name="password_reset_complete")
]
