from django.contrib import admin
from .models import drawpage, drawsteps

# Inline admin for drawsteps inside drawpage
class drawstepsInline(admin.TabularInline):
    model = drawsteps
    extra = 1   # how many empty rows to show for adding new steps
    fields = ('stepno', 'steptext', 'image')  # fields shown inline

@admin.register(drawpage)
class drawpageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    inlines = [drawstepsInline]   # ✅ show steps inline

@admin.register(drawsteps)
class drawstepsAdmin(admin.ModelAdmin):
    list_display = ('id', 'stepcontent', 'stepno', 'steptext', 'image')
    list_filter = ('stepcontent',)
    search_fields = ('steptext',)
