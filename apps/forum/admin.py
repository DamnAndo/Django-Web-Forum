from django.contrib import admin
from .models import Forum,Comment

# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment

class ForumAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]
    
admin.site.register(Forum,ForumAdmin)
