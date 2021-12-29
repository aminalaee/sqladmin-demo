from sqladmin import ModelAdmin

from models import User, Address


class UserAdmin(ModelAdmin, model=User):
    name = "User"
    column_list = [User.id, User.name, User.email]


class AddressAdmin(ModelAdmin, model=Address):
    name_plural = "Addresses"
    column_list = ["id", "country", "city", "zipcode", "user_id"]
