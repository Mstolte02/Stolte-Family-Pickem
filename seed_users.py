from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()

    existing = User.query.all()
    print("Before adding:", existing)

    u = User(name="Mark Stolte", email="mark@example.com")
    db.session.add(u)
    db.session.commit()

    after = User.query.all()
    print("After adding:", after)
