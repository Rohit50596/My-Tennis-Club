from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","phone",)
   # prepopulated_fields={"slug":("firstname","lastname")}

admin.site.register(Member,MemberAdmin)
# Register your models here.
