from django.contrib import admin
from firstapp.models import User , Community,Role,Member,Post,Comment
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','email','password','creat_at']
admin.site.register(User,UserAdmin)
# admin.site.register(User)
admin.site.register(Community)
admin.site.register(Role)
admin.site.register(Member)
admin.site.register(Post)
admin.site.register(Comment)
