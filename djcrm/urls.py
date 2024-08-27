from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (LoginView,  PasswordResetView, PasswordResetDoneView, 
                                       PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.urls import path, include
from leads.views import LandingPageView, SignUpView, logoutview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('leads/' , include('leads.urls' , namespace='leads')),
    path('agents/' , include('agents.urls' , namespace='agents')),
    path('login/', LoginView.as_view(), name='login'),
    path("reset-password/", PasswordResetView.as_view(), name="reset-password"),
    path("password-reset-done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset-complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("password-reset-confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('logout/',logoutview, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),    
]
if settings.DEBUG==True:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
