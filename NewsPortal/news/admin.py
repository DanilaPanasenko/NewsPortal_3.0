from django.contrib import admin
from .models import Post, Category, Author, PostCategory, Comment
from modeltranslation.admin import TranslationAdmin # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)


# Регистрируем модели для перевода в админке

class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)

