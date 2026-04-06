from django.contrib import admin
from django.utils.html import format_html

from apps.accounts.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff', 'is_active')
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_active')
    readonly_fields = ('access_token_preview',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('JWT', {'fields': ('access_token_preview',)}),
    )

    @admin.display(description='Access token')
    def access_token_preview(self, obj):
        if not obj or not obj.pk:
            return 'Save user first to generate token.'

        token = str(RefreshToken.for_user(obj).access_token)
        return format_html(
            '<textarea rows="6" style="width:100%;font-family:monospace;">{}</textarea>',
            token,
        )


admin.site.register(User, UserAdmin)