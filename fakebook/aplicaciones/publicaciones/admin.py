from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'image')
	readonly_fields = ('created', 'updated')



admin.site.register(Post, PostAdmin)

"""
    class Media:
        css = {
            'all': ('publicaciones/css/cusm_ckeditor.css',)
        }
"""
