from flask import Flask
import mysql.connector

app = Flask(__name__)

with open("/vault/secrets/mysql", "r") as f:
    MYSQL_PASSWORD = f.read().strip()

def get_connection():
    return mysql.connector.connect(
        host="mysql-0.mysql.default.svc.cluster.local",
        user="root",
        password=MYSQL_PASSWORD,
        database="demo"
    )

@app.route('/')
def home():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users where name="Loki"")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    result = [row[0] for row in rows]

    return f"Showing all the users in database: {', '.join(result)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
