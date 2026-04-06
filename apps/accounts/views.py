from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class WebLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = False


class SignUpView(TemplateView):
    template_name = 'accounts/signup.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if password1 != password2:
            return self.render_to_response({
                'form_data': {'username': username, 'email': email},
                'errors': ['Passwords do not match.'],
            })

        serializer = RegisterSerializer(data={
            'username': username,
            'email': email,
            'password': password1,
        })
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('web-login')

        error_list = []
        for field_errors in serializer.errors.values():
            for err in field_errors:
                error_list.append(str(err))

        return self.render_to_response({
            'form_data': {'username': username, 'email': email},
            'errors': error_list,
        })


class HomeRedirectView(View):
    def get(self, request, *args, **kwargs):
        return redirect('web-login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    login_url = 'web-login'

    def post(self, request, *args, **kwargs):
        user = request.user
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()

        if not username:
            messages.error(request, 'Username is required.')
            return self.render_to_response({'form_data': request.POST})

        username_taken = User.objects.exclude(pk=user.pk).filter(username=username).exists()
        if username_taken:
            messages.error(request, 'This username is already taken.')
            return self.render_to_response({'form_data': request.POST})

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save(update_fields=['username', 'email', 'first_name', 'last_name'])
        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')


