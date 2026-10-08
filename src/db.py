import psycopg2

# Hardcoded creds — temporary, will fix later
conn = psycopg2.connect(
    host="~[PY_HARDCODED_HOST_0]~",
    database="myapp",
    user="admin",
    password="~[URL_EMBEDDED_PASSWORD_0]~"
)

ADMIN_EMAIL = "~[EMAIL_1]~"
SUPPORT_EMAIL = "~[EMAIL_0]~"

def get_user(user_id: int):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    return cur.fetchone()
