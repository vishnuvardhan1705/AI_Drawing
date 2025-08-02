from django.contrib import admin
from .models import drawpage,drawsteps


@admin.register(drawpage)
class drawpageAdmin(admin.ModelAdmin):
    list_display=('id','name','description')

@admin.register(drawsteps)
class drawstepsAdmin(admin.ModelAdmin):
    list_display=('id','stepcontent','stepno','image','steptext')
    list_filter=('stepcontent',)


