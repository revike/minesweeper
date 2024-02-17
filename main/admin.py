from django.contrib import admin

from main.forms import GameAdminForm
from main.models import Game, GameField
from settings.settings import FRONT_URL

admin.site.site_header = 'Minesweeper administrator'
admin.site.site_url = FRONT_URL


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
    readonly_fields = ['completed', 'created_at', 'updated_at']

    def has_change_permission(self, request, obj=None):
        pass
