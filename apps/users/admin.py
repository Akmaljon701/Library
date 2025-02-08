from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from apps.users.models import CustomUser

admin.site.site_title = "Library Admin"
admin.site.site_header = "Library"
admin.site.index_title = "Library Admin"
admin.site.site_brand = "Library"
admin.site.welcome_sign = "Library"
admin.site.copyright = "Library"

admin.site.unregister(Group)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ['username']
    list_display = ['id', 'username', 'role', 'created_at', 'is_active']
    list_display_links = ['username',]
    list_filter = ['is_active', 'role']
    fieldsets = (
        (None, {'fields': ('username', 'role')}),
        ('Personal info', {'fields': ('device_tokens',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ['username',]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.order_by('-created_at')


admin.site.register(CustomUser, CustomUserAdmin)

