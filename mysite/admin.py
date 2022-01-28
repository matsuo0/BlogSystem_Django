from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.models.account_models import User
from mysite.models.profile_models import Profile

from mysite.forms import UserCreationForm  # adminでuser作成用に追加


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'is_active',
                'is_admin',
            )
        })
    )
    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    # --- adminでuser作成用に追加 ---
    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    # --- adminでuser作成用に追加 ---

    add_form = UserCreationForm  # adminでuser作成用に追加

    inlines = (ProfileInline, ) # ProfileモデルはUserモデルとOneToOneでひもづいている。


admin.site.unregister(Group)  # 表示されないように
admin.site.register(User, CustomUserAdmin)

# admin.site.register(Profile)
