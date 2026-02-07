from src.database import get_connection

def save_history(user_id, job_text, label, confidence):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO history (user_id, job_text, label, confidence) VALUES (?, ?, ?, ?)",
        (user_id, job_text, label, confidence)
    )

    conn.commit()
    conn.close()

def get_history(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, job_text, label, confidence FROM history WHERE user_id=?",
        (user_id,)
    )

    rows = cur.fetchall()
    conn.close()
    return rows

def delete_history(record_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM history WHERE id=?", (record_id,))
    conn.commit()
    conn.close()
