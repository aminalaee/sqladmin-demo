from sqladmin import ModelAdmin

from models import User, Address


class UserAdmin(ModelAdmin, model=User):
    name = "User"
    list_display = [User.id, User.name, User.email]


class AddressAdmin(ModelAdmin, model=Address):
    name_plural = "Addresses"
    list_display = ["id", "country", "city", "zipcode", "user_id"]
