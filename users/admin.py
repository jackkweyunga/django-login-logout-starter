from django.contrib import admin
from django.shortcuts import redirect, render

from .models import User
from django.urls import path, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.utils.html import format_html
# Register your models here.
from django.contrib.auth.forms import PasswordChangeForm



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("email", "first_name", "last_name")
    list_filter = ("is_active", "date_joined", "last_login")
    search_fields = ("email", "first_name", "last_name", "last_login")
    fieldsets = (
        (
            "PERSONAL INFORMATION",
            {"fields": ("username", "email", "first_name", "last_name", "password")},
        ),
        (
            "GROUPS AND PERMISSION",
            {
                "classes": ("collapse",),
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "DATES",
            {
                "classes": ("collapse",),
                "fields": ("last_login", "date_joined"),
            },
        ),
        (
            "STATUS",
            {
                "classes": ("collapse",),
                "fields": ("is_superuser", "is_active", "is_staff"),
            },
        ),
    )
    
    ##########---------------#########
    #change password action in admin
   
    def change_password(self, request, user_id, form_url=''):
        user = self.get_object(request, user_id)
        if request.method == 'POST':
            form = PasswordChangeForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin:index')
        else:
            form = PasswordChangeForm(user)
            
        context={'form': form, 'user_id': user_id}
        return PasswordChangeView.as_view()(request=request, extra_context=context)
        
        
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<path:user_id>/change_password/', self.admin_site.admin_view(self.change_password), name='user_change_password'),
        ]
        return custom_urls + urls
        
    def user_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Change password</a>',
            reverse('admin:user_change_password', args=[obj.pk])
        )
    user_actions.short_description = 'Actions'
    
    def get_list_display(self, request):
        list_display = super().get_list_display(request)
        if request.user.is_superuser:
            list_display += ('user_actions',)
        return list_display

 
    ##########---------------#########
    #custom actions
    actions = ["make_inactive", "make_active"]

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = "Make selected users inactive"

    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = "Make selected users active"

