from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import database

router = APIRouter()

class TeamSelection(BaseModel):
    user_id: int
    match_id: int
    player_ids: list[int]

class ScoreUpdate(BaseModel):
    match_id: int
    player_scores: dict

@router.post("/select_team")
def select_team(selection: TeamSelection):
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO selections (user_id, match_id, player_ids, timestamp) VALUES (?, ?, ?, ?)''',
                   (selection.user_id, selection.match_id, str(selection.player_ids), datetime.utcnow()))
    conn.commit()
    conn.close()
    return {"message": "Team selection saved."}

@router.get("/leaderboard")
def leaderboard():
    conn = database.get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, SUM(total_score) as total FROM scores GROUP BY user_id ORDER BY total DESC")
    results = cursor.fetchall()
    conn.close()
    return {"leaderboard": [dict(row) for row in results]}
