from faker import Faker
from sqladmin import Admin
from starlette.applications import Starlette
from starlette.responses import RedirectResponse
from starlette.routing import Route

from admin import UserAdmin, AddressAdmin
from models import db, Base, engine, User, Address


def startup():
    Base.metadata.create_all(engine)
    faker = Faker()

    for _ in range(100):
        user = User(name=faker.name(), email=faker.email())
        db.add(user)
        db.flush()

        address = Address(
            city=faker.city(),
            country=faker.country(),
            zipcode=faker.zipcode(),
            user_id=user.id,
        )

        db.add(address)

    db.commit()


def shutdown():
    Base.metadata.drop_all(engine)


app = Starlette(
    on_startup=[startup],
    on_shutdown=[shutdown],
    routes=[
        Route("/", endpoint=RedirectResponse(url="/admin")),
    ],
)
admin = Admin(app=app, db=db)

admin.register_model(UserAdmin)
admin.register_model(AddressAdmin)
