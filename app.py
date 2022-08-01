import os
import uvicorn
from faker import Faker
from sqladmin import Admin
from starlette.applications import Starlette
from starlette.responses import RedirectResponse
from starlette.routing import Route

from admin import UserAdmin, AddressAdmin, ProfileAdmin
from models import db, Base, engine, User, Address, Profile


def startup():
    faker = Faker()

    try:
        Base.metadata.create_all(engine)

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

            profile = Profile(
                user=user,
                metadata=faker.sentence(),
            )

            db.add(address)
            db.add(profile)
        db.commit()
    except Exception:
        pass


def shutdown():
    Base.metadata.drop_all(engine)


app = Starlette(
    on_startup=[startup],
    on_shutdown=[shutdown],
    routes=[
        Route("/", endpoint=RedirectResponse(url="/admin")),
    ],
)
admin = Admin(app=app, engine=engine)

admin.register_model(UserAdmin)
admin.register_model(AddressAdmin)
admin.register_model(ProfileAdmin)


if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        log_level="info",
        workers=2,
    )
