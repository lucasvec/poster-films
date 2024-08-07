import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        "postgres://avnadmin:AVNS_nAuWxYUuoklgWIaoKYg@cinemar1-cinemar1.l.aivencloud.com:23598/defaultdb?sslmode=require",
        sslmode="require"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM movies;')
    moviesFet = cur.fetchall()
    cur.close()
    conn.close()
    
    movies = []
    for row in moviesFet:
        movies.append({"name": row[0], "rating": row[1]})

    return render_template('index.html', movies=movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
