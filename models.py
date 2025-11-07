from app import db
from werkzeug.security import generate_password_hash, check_password_hash



import secrets

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120))
    password_hash = db.Column(db.String(128))
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    access_code = db.Column(db.String(50))

    # helper functions
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.name}>"




class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer, nullable=False)
    home_team = db.Column(db.String(50), nullable=False)
    away_team = db.Column(db.String(50), nullable=False)
    kickoff = db.Column(db.String(50))  # optional for now
    winner = db.Column(db.String(50))   # can be null until the game ends

    def __repr__(self):
        return f"<Game Week {self.week}: {self.away_team} at {self.home_team}>"

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    abbreviation = db.Column(db.String(5), unique=True, nullable=False)
    primary_color = db.Column(db.String(7))   # hex code like "#00338D"
    secondary_color = db.Column(db.String(7))
    logo_url = db.Column(db.String(255))      # link to team logo

    def __repr__(self):
        return f"<Team {self.name}>"

class Pick(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    picked_team = db.Column(db.String(50), nullable=False)
    is_correct = db.Column(db.Boolean, default=None)  # null until game ends

    user = db.relationship('User', backref='picks', lazy=True)
    game = db.relationship('Game', backref='picks', lazy=True)

    def __repr__(self):
        return f"<Pick {self.user.name} → {self.picked_team}>"
