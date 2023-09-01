from django.contrib import admin
from users.models.user import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'email', 'password')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 25
