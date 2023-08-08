from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import Customer, Message


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-id',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('ad', 'mail', 'telefon', 'status')
    list_editable = ('status',)
    actions = ['mark_as_read', 'mark_as_unread']

    @admin.action(description="Oxunmuş kimi işarələ")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, "Seçilmiş mesajlar oxunmuş kimi işarələndi.", messages.SUCCESS)

    @admin.action(description="Oxunmamış kimi işarələ")
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, "Seçilmiş mesajlar oxunmamış kimi işarələndi.", messages.SUCCESS)



