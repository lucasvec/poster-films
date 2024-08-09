import os
import psycopg2
from flask import Flask, render_template
from dotenv import load_dotenv

app = Flask(__name__)

def get_db_connection():
    load_dotenv()
    conn = psycopg2.connect(os.getenv("DB_URL"))
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM movies;')
    movies = [] 
    moviesFet = cur.fetchall()
    cur.close()
    conn.close()
    
    """
    HTML (<li>) de todos os dados.
    """
    html = ""
    
    for row in moviesFet:
        movies.append({"name": row[0], "rating": row[1]})
    
    for movie in movies:
    
        html = html + """
            <li class="list-group-item">
                <span class="badge">%s
                    <span class="glyphicon glyphicon-star"></span>
                </span>
                %s
            </li>
        """ % (movie['rating'], movie['name'])
       
    return open('webapp/templates/index.html').read()  % (html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)