import database
from datetime import datetime

def fetch_match_stats(match_id: int):
    # Replace with real API
    return {
        101: 120,
        102: 80,
        103: 45
    }

def update_scores(match_id):
    match_stats = fetch_match_stats(match_id)
    conn = database.get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT user_id, player_ids FROM selections WHERE match_id = ?", (match_id,))
    selections = cursor.fetchall()

    for selection in selections:
        user_id = selection["user_id"]
        players = eval(selection["player_ids"])
        total_score = sum([match_stats.get(pid, 0) for pid in players])
        cursor.execute('''INSERT INTO scores (match_id, user_id, total_score, timestamp) VALUES (?, ?, ?, ?)''',
                       (match_id, user_id, total_score, datetime.utcnow()))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    match_id = 1  # Example match
    update_scores(match_id)
