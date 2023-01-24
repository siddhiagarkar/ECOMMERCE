from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('searcheditems/', views.searchview, name='searched_item'),
    path('genderfiltereditems/', views.filterview, name='products_by_gender'),
    path('colourfiltereditems/', views.colorview, name='products_by_colours'),
    path('register/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='register'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)