from django.contrib import admin
from books.models import *
# Register your models here.

@admin.register(contact)
class contactadmin(admin.ModelAdmin):
    list_display=('name','email','Mobileno','message')

@admin.register(service)
class serviceadmin(admin.ModelAdmin):
    pass

@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    pass

@admin.register(author)
class authoradmin(admin.ModelAdmin):
    pass

@admin.register(subscribe)
class subscribeadmin(admin.ModelAdmin):
    list_display=('Email',)

@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    pass

@admin.register(book)
class bookadmin(admin.ModelAdmin):
    pass

@admin.register(faq)
class faqadmin(admin.ModelAdmin):
    pass

@admin.register(issuebook)
class issuebookadmin(admin.ModelAdmin):
    pass

@admin.register(Ordernow)
class Ordernowadmin(admin.ModelAdmin):
    pass