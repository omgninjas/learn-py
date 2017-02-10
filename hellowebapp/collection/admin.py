from django.contrib import admin

# import your model
from collection.models import Quote

# set up automated slug creation
class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ('author', 'blockquote', 'source',)
    prepopulated_fields = {'slug' : ('author',)}

# Register your models here.
admin.site.register(Quote, QuoteAdmin)