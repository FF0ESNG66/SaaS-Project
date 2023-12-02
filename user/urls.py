from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    
    path('login/', auth_views.LoginView.as_view(template_name="user/login.html",
                                                next_page='course:course-list'),
                                                name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(email_template_name = "user/password_reset_email.html",
                                                                 success_url = reverse_lazy("user:password-reset-done")),
                                                                 name = 'password-reset'),

    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy("user:password-reset-complete")), name='password-reset-confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user:password-change-done')), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password-change-done'),
]