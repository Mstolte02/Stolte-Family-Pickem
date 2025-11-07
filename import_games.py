import pandas as pd
from app import create_app, db
from app.models import Game

app = create_app()

# Load Excel
df = pd.read_excel("nfl_games_2025.xlsx", sheet_name="Games")

with app.app_context():
    db.create_all()
    for _, row in df.iterrows():
        existing = Game.query.filter_by(week=row['week'], home_team=row['home_team'], away_team=row['away_team']).first()
        if not existing:
            g = Game(
                week=int(row['week']),
                home_team=row['home_team'],
                away_team=row['away_team'],
                winner=row.get('winner') if pd.notna(row.get('winner')) else None,
                kickoff=str(row.get('kickoff')) if pd.notna(row.get('kickoff')) else None
            )
            db.session.add(g)
    db.session.commit()
    print(f"Imported {len(df)} games!")
