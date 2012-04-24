from django.contrib import admin
from library.members.models import Group, Member

admin.site.register(Group)
admin.site.register(Member)