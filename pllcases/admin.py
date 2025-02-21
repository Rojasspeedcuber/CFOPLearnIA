from django.contrib import admin
from pllcases.models import PLL_Cases


class PLLadmin(admin.ModelAdmin):
    list_display = ('cases', 'algorithm')
    search_fields = ('cases',)


admin.site.register(PLL_Cases, PLLadmin)
