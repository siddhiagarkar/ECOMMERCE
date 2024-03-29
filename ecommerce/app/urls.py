from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.store, name='store'),
    path('profile/', views.profile, name='profile'),
    path('sale/', views.sale_view, name='sales'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('searcheditems/', views.searchview, name='searched_item'),
    path('genderfiltereditems/', views.filterview, name='products_by_gender'),
    path('colourfiltereditems/', views.colorview, name='products_by_colours'),
    path('sort-by/', views.sortview, name='sorted_products'),
    path('register/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='register'),
    path('wishlist/', views.wishlistview, name='wishlist'),
    path('product/<int:myid>', views.productview, name='product'),
    # path('msg-submitted/', views.store, name='mes'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)