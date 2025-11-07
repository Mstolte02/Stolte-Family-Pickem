from app import create_app, db
from app.models import User

app = create_app()

names = [
    "Debbie", "Dee", "Johnny", "Sarah", "Liz", "Cam", "Mark C.", "Rachel",
    "Mark E.", "Angie", "Payton", "Melissa", "Benny", "Matt", "Levi", "Deklyn", "Tommy"
]

with app.app_context():
    db.create_all()
    for name in names:
        # skip if already exists
        if not User.query.filter_by(name=name).first():
            u = User(name=name, email=f"{name.lower().replace(' ', '')}@example.com")
            db.session.add(u)
    db.session.commit()
    print("All players added!")
