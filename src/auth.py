from src.database import get_connection, hash_password

def signup_user(email, password):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, hash_password(password))
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login_user(email, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM users WHERE email=? AND password=?",
        (email, hash_password(password))
    )
    user = cur.fetchone()
    conn.close()

    return user[0] if user else None
