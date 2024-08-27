from django.contrib import admin

from .models import User, Agent, Lead, UserProfile, Category

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    model = User

class LeadInlineModel(admin.TabularInline):
    model = Lead


@admin.register(Agent)

class UserAdmin(admin.ModelAdmin):
    model = User

    inlines = [LeadInlineModel]


admin.site.register(Lead)

admin.site.register(UserProfile)

admin.site.register(Category)