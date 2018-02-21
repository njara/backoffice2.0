from django.contrib import admin
from .models import *
from django import forms
from django.contrib.auth.admin import UserAdmin

admin.site.register(Company)
admin.site.register(Card)
admin.site.register(Emisor)
admin.site.register(Device)
admin.site.register(Account)


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileUserAdmin(UserAdmin):
    # The forms to add and change user instances
    add_form = UserCreationForm
    list_display = ("username",)
    ordering = ("username",)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'is_active')}
            ),
        )

    filter_horizontal = ()

admin.site.register(UserProfile, ProfileUserAdmin)
