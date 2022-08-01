from sqladmin import ModelAdmin

from models import User, Address, Profile


class UserAdmin(ModelAdmin, model=User):
    name = "User"
    column_list = [User.id, User.name, User.email]


class AddressAdmin(ModelAdmin, model=Address):
    name_plural = "Addresses"
    column_list = ["id", "country", "city", "zipcode", "user"]


class ProfileAdmin(ModelAdmin, model=Profile):
    column_list = [Profile.id, Profile.user, Profile.user_id]
