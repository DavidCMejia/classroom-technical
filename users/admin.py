from django.contrib import admin

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'email', 'password')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_per_page = 25