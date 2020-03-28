from django.contrib import admin

from django_jalali.admin.filters import JDateFieldListFilter

#you need import this for adding jalali calander widget
import django_jalali.admin as jadmin
from webroot.models import exp, income, token


class expAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', JDateFieldListFilter),
    )
admin.site.register(exp, expAdmin)
class incomeAdmin(admin.ModelAdmin):
    list_filter = (
        ('date', JDateFieldListFilter),
    )

admin.site.register(income, incomeAdmin)
admin.site.register(token)
