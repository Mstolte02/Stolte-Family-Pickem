from app import create_app, db
from app.models import User
import random

app = create_app()

with app.app_context():
    users = User.query.all()
    print("🔐 Generating passwords for all users...\n")

    for user in users:
        rand_num = random.randint(100, 999)
        base_name = user.name.split()[0].capitalize()
        password = f"{base_name}{rand_num}"
        user.set_password(password)
        print(f"{user.name}: {password}")

    db.session.commit()
    print("\n✅ All passwords generated and saved!")
