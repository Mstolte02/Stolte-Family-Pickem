from app import create_app
from app.models import User

app = create_app()

with app.app_context():
    for u in User.query.all():
        print(f"{u.name}: http://127.0.0.1:5000/picks/{u.access_code}")
