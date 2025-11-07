from app import create_app, db
from app.models import User

app = create_app()

records = {
"Debbie": (56,37),
"Dee": (58,35),
"Johnny": (59,34),
"Sarah": (57,36),
"Liz": (47,46),
"Cam": (59,34),
"Mark C.": (64,29),
"Rachel": (54,39),
"Mark E.": (62,31),
"Angie": (47,46),
"Payton": (52,41),
"Melissa": (56,37),
"Benny": (46,47),
"Matt": (52,41),
"Levi": (53,40),
"Deklyn": (53,40),
"Tommy": (63,30)
}

with app.app_context():
    for name, (wins, losses) in records.items():
        user = User.query.filter_by(name=name).first()
        if user:
            user.wins = wins
            user.losses = losses
    db.session.commit()
    print("Records updated successfully!")
