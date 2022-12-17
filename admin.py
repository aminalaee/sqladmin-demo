from sqladmin import ModelAdmin

from models import User, Address, Profile


class UserAdmin(ModelAdmin, model=User):
    name = "User"
    icon = "fa fa-user"
    column_list = [User.id, User.name, User.email]
    column_searchable_list = [User.name, User.email]
    save_as = True


class AddressAdmin(ModelAdmin, model=Address):
    name_plural = "Addresses"
    icon = "fa fa-address-card"
    column_list = ["id", "country", "city", "zipcode", "user"]
    column_searchable_list = [Address.country]


class ProfileAdmin(ModelAdmin, model=Profile):
    icon = "fa fa-user"
    column_list = [Profile.id, Profile.user, Profile.user_id]
