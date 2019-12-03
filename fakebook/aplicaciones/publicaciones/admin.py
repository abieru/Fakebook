from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('image',)
	readonly_fields = ('created', 'updated')

	class Meta:
	    css = {
	        'all':('publicaciones/css/custom_ckeditor.css',)
	    }
        

admin.site.register(Post, PostAdmin)

"""
    class Media:
        css = {
            'all': ('publicaciones/css/custom_ckeditor.css',)
        }
"""
