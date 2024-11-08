"""
URL configuration for codesphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name="signup"),
    path('profile/edit',views.UserProfileEditView.as_view(),name="profile-edit"),
    path('signin/',views.signInView.as_view(),name="signin"),
    path('index/',views.IndexView.as_view(),name="index"),
    path('logout/',views.LogOutView.as_view(),name="logout"),
    path('project/create/',views.ProjectCreateView.as_view(),name="project-create"),
    path('myworks/all/',views.ProjectListView.as_view(),name="myworks"),
    path('project/<int:pk>/change/',views.ProjectUpdateView.as_view(),name="project-update"),
    path('project/<int:pk>/detail/',views.ProjectDetailView.as_view(),name="project-detail"),
    path('project/<int:pk>/addtowhishlist/',views.AddtoWishlistView.as_view(),name="add-to-whishlist"),
    path('project/wishlist/all',views.WishlistItemView.as_view(),name="mywishlist"),
    path('wishlist/<int:pk>/delete/',views.WishListItemDeleteView.as_view(),name="delete-item"),
    path('checkout',views.CheckOutView.as_view(),name="checkout"),
    path('payment/verify',views.PaymentVerificationView.as_view(),name="verify-payment"),
    path('orders/all/',views.MyOrderView.as_view(),name="orders"),
    path('password/reset',views.PasswordResetView.as_view(),name="reset")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
