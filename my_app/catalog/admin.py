
from django.contrib import admin
from .models import Category, Skill


class CategoryAdmin(admin.ModelAdmin):
    pass

class SkillAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Skill, SkillAdmin)
