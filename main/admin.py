from django.contrib import admin

from main.forms import GameAdminForm
from main.models import Game, GameField


class GameFieldInline(admin.StackedInline):
    """Game Field Inline"""
    model = GameField
    extra = 0
    max_num = 1
    can_delete = False

    def has_change_permission(self, request, obj=None):
        pass

    def has_delete_permission(self, request, obj=None):
        pass

    def has_add_permission(self, request, obj):
        pass


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Game Admin"""
    inlines = [GameFieldInline]
    form = GameAdminForm
    readonly_fields = ['completed']

    def has_change_permission(self, request, obj=None):
        pass