from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User, Game, Team, Pick
from app.forms import PickForm
from app import db

main = Blueprint('main', __name__)

# -------------------------------------------------------
# 🏠 HOME PAGE
# -------------------------------------------------------
@main.route('/')
def home():
    users = User.query.order_by(User.name).all()
    return render_template('index.html', users=users)


# -------------------------------------------------------
# 👤 LOGIN / LOGOUT
# -------------------------------------------------------
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(name=name).first()
        if user and user.check_password(password):
            flash(f"Welcome, {user.name}!", "success")
            return redirect(url_for('main.make_picks', username=user.name))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for('main.login'))

    return render_template('login.html')



@main.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))


# -------------------------------------------------------
# ✍️ MAKE PICKS (requires login)
# -------------------------------------------------------
@main.route('/picks/<username>', methods=['GET', 'POST'])
def make_picks(username):
    user = User.query.filter_by(name=username).first_or_404()
    games = Game.query.all()

    forms = []
    for game in games:
        form = PickForm(prefix=str(game.id))
        form.pick.choices = [
            (game.home_team, game.home_team),
            (game.away_team, game.away_team)
        ]
        forms.append((game, form))

    if request.method == 'POST':
        for game, form in forms:
            if form.validate_on_submit():
                existing = Pick.query.filter_by(user_id=user.id, game_id=game.id).first()
                if existing:
                    existing.picked_team = form.pick.data
                else:
                    new_pick = Pick(user_id=user.id, game_id=game.id, picked_team=form.pick.data)
                    db.session.add(new_pick)
        db.session.commit()
        flash("Picks saved!", "success")
        return redirect(url_for('main.make_picks', username=username))

    teams = {t.name.split()[-1]: t for t in Team.query.all()}
    return render_template('make_picks.html', user=user, forms=forms, teams=teams)



# -------------------------------------------------------
# 👥 USERS LIST
# -------------------------------------------------------
@main.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)


# -------------------------------------------------------
# 🏈 GAMES PAGE (with week filter)
# -------------------------------------------------------
@main.route('/games')
def games():
    week = request.args.get('week', type=int)

    if week:
        games = Game.query.filter_by(week=week).order_by(Game.id).all()
    else:
        games = Game.query.order_by(Game.week, Game.id).all()

    weeks = sorted({g.week for g in Game.query.all()})

    teams = {t.name: t for t in Team.query.all()}
    for team in list(teams.values()):
        nickname = team.name.split()[-1]
        teams[nickname] = team

    return render_template('games.html', games=games, teams=teams, weeks=weeks, selected_week=week)


# -------------------------------------------------------
# 📋 ALL PICKS PAGE (with week filter)
# -------------------------------------------------------
@main.route('/all_picks')
def all_picks():
    week = request.args.get('week', type=int)

    if week:
        games = Game.query.filter_by(week=week).order_by(Game.id).all()
    else:
        games = Game.query.order_by(Game.week, Game.id).all()

    users = User.query.order_by(User.name).all()
    picks = Pick.query.all()

    pick_lookup = {(p.user_id, p.game_id): p.picked_team for p in picks}
    weeks = sorted({g.week for g in Game.query.all()})

    return render_template(
        'all_picks.html',
        games=games,
        users=users,
        pick_lookup=pick_lookup,
        weeks=weeks,
        selected_week=week
    )


# -------------------------------------------------------
# 🛠️ ADMIN RESULTS (password: enter0202)
# -------------------------------------------------------
@main.route('/admin/results', methods=['GET', 'POST'])
def update_results():
    password = request.args.get('password')
    if password != "enter0202":
        return (
            "<h2 style='text-align:center;color:red;'>Access Denied</h2>"
            "<p style='text-align:center;'>You must provide the correct password in the URL, e.g.: "
            "<code>?password=enter0202</code></p>",
            403,
        )

    games = Game.query.order_by(Game.week, Game.id).all()

    if request.method == 'POST':
        for game in games:
            winner = request.form.get(f'winner_{game.id}')
            if winner:
                game.winner = winner
        db.session.commit()

        for pick in Pick.query.all():
            pick.is_correct = None
            if pick.game.winner and pick.picked_team == pick.game.winner:
                pick.is_correct = True
            elif pick.game.winner and pick.picked_team != pick.game.winner:
                pick.is_correct = False
        db.session.commit()

    return render_template('update_results.html', games=games)


# -------------------------------------------------------
# 🏆 LEADERBOARD (with week filter)
# -------------------------------------------------------
@main.route('/leaderboard')
def leaderboard():
    week = request.args.get('week', type=int)
    users = User.query.all()
    standings = []

    for user in users:
        base_wins = user.wins or 0
        base_losses = user.losses or 0

        query = Pick.query.filter_by(user_id=user.id)
        if week:
            query = query.join(Game).filter(Game.week == week)

        picks = query.all()
        new_wins = len([p for p in picks if p.is_correct is True])
        new_losses = len([p for p in picks if p.is_correct is False])

        total_wins = base_wins + new_wins
        total_losses = base_losses + new_losses
        total_games = total_wins + total_losses
        pct = round((total_wins / total_games) * 100, 1) if total_games > 0 else 0.0

        standings.append({
            "name": user.name,
            "wins": total_wins,
            "losses": total_losses,
            "pct": pct
        })

    standings.sort(key=lambda x: (-x["wins"], x["losses"], x["name"]))
    weeks = sorted({g.week for g in Game.query.all()})

    return render_template('leaderboard.html', standings=standings, weeks=weeks, selected_week=week)
