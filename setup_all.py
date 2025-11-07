import subprocess

scripts = [
    "init_db.py",
    "seed_teams.py",
    "seed_users.py",
    "seed_records.py",
    "update_users_table.py",
    "generate_passwords.py",
    "generate_links.py",
    "import_games.py",
    "seed_games.py",
    "seed_players.py",
    "check_users.py"
]

print("🚀 Starting full setup sequence...\n")

for script in scripts:
    print(f"▶️ Running {script} ...")
    result = subprocess.run(["python3.9", script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ {script} completed successfully!\n")
        if result.stdout.strip():
            print(result.stdout.strip(), "\n")
    else:
        print(f"❌ Error running {script}:")
        print(result.stderr)
        break

print("🎉 Setup complete! Launch your app with:")
print("   python3.9 run.py")
