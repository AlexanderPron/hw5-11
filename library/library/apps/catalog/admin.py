from django.contrib import admin
from .models import Author, Book, PublishingHouse

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # @staticmethod
    # def author_full_name(obj):
    #     return obj.author.full_name
    list_display = ('title', 'author')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'ph_name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass