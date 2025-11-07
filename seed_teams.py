from app import create_app, db
from app.models import Team

app = create_app()

teams = [
    {"name": "Cardinals", "abbreviation": "ARI", "primary_color": "#97233F", "secondary_color": "#000000", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/ari.png"},
    {"name": "Falcons", "abbreviation": "ATL", "primary_color": "#A71930", "secondary_color": "#000000", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/atl.png"},
    {"name": "Ravens", "abbreviation": "BAL", "primary_color": "#241773", "secondary_color": "#000000", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/bal.png"},
    {"name": "Bills", "abbreviation": "BUF", "primary_color": "#00338D", "secondary_color": "#C60C30", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/buf.png"},
    {"name": "Panthers", "abbreviation": "CAR", "primary_color": "#0085CA", "secondary_color": "#101820", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/car.png"},
    {"name": "Bears", "abbreviation": "CHI", "primary_color": "#0B162A", "secondary_color": "#C83803", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/chi.png"},
    {"name": "Bengals", "abbreviation": "CIN", "primary_color": "#FB4F14", "secondary_color": "#000000", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/cin.png"},
    {"name": "Browns", "abbreviation": "CLE", "primary_color": "#311D00", "secondary_color": "#FF3C00", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/cle.png"},
    {"name": "Cowboys", "abbreviation": "DAL", "primary_color": "#041E42", "secondary_color": "#869397", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/dal.png"},
    {"name": "Broncos", "abbreviation": "DEN", "primary_color": "#FB4F14", "secondary_color": "#002244", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/den.png"},
    {"name": "Lions", "abbreviation": "DET", "primary_color": "#0076B6", "secondary_color": "#B0B7BC", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/det.png"},
    {"name": "Packers", "abbreviation": "GB", "primary_color": "#203731", "secondary_color": "#FFB612", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/gb.png"},
    {"name": "Texans", "abbreviation": "HOU", "primary_color": "#03202F", "secondary_color": "#A71930", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/hou.png"},
    {"name": "Colts", "abbreviation": "IND", "primary_color": "#002C5F", "secondary_color": "#A2AAAD", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/ind.png"},
    {"name": "Jaguars", "abbreviation": "JAX", "primary_color": "#006778", "secondary_color": "#9F792C", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/jax.png"},
    {"name": "Chiefs", "abbreviation": "KC", "primary_color": "#E31837", "secondary_color": "#FFB81C", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/kc.png"},
    {"name": "Raiders", "abbreviation": "LV", "primary_color": "#000000", "secondary_color": "#A5ACAF", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/lv.png"},
    {"name": "Chargers", "abbreviation": "LAC", "primary_color": "#0080C6", "secondary_color": "#FFC20E", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/lac.png"},
    {"name": "Rams", "abbreviation": "LAR", "primary_color": "#003594", "secondary_color": "#FFA300", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/lar.png"},
    {"name": "Dolphins", "abbreviation": "MIA", "primary_color": "#008E97", "secondary_color": "#F26A24", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/mia.png"},
    {"name": "Vikings", "abbreviation": "MIN", "primary_color": "#4F2683", "secondary_color": "#FFC62F", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/min.png"},
    {"name": "Patriots", "abbreviation": "NE", "primary_color": "#002244", "secondary_color": "#C60C30", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/ne.png"},
    {"name": "Saints", "abbreviation": "NO", "primary_color": "#D3BC8D", "secondary_color": "#101820", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/no.png"},
    {"name": "Giants", "abbreviation": "NYG", "primary_color": "#0B2265", "secondary_color": "#A71930", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/nyg.png"},
    {"name": "Jets", "abbreviation": "NYJ", "primary_color": "#125740", "secondary_color": "#000000", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/nyj.png"},
    {"name": "Eagles", "abbreviation": "PHI", "primary_color": "#004C54", "secondary_color": "#A5ACAF", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/phi.png"},
    {"name": "Steelers", "abbreviation": "PIT", "primary_color": "#FFB612", "secondary_color": "#101820", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/pit.png"},
    {"name": "49ers", "abbreviation": "SF", "primary_color": "#AA0000", "secondary_color": "#B3995D", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/sf.png"},
    {"name": "Seahawks", "abbreviation": "SEA", "primary_color": "#002244", "secondary_color": "#69BE28", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/sea.png"},
    {"name": "Buccaneers", "abbreviation": "TB", "primary_color": "#D50A0A", "secondary_color": "#0A0A08", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/tb.png"},
    {"name": "Titans", "abbreviation": "TEN", "primary_color": "#4B92DB", "secondary_color": "#0C2340", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/ten.png"},
    {"name": "Commanders", "abbreviation": "WAS", "primary_color": "#773141", "secondary_color": "#FFB612", "logo_url": "https://a.espncdn.com/i/teamlogos/nfl/500/was.png"}
]

with app.app_context():
    db.create_all()
    for t in teams:
        if not Team.query.filter_by(name=t["name"]).first():
            db.session.add(Team(**t))
    db.session.commit()
    print("Seeded all NFL teams!")
