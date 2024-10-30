from flask import Flask, render_template, jsonify
import os
from film import Film

import psycopg2
import psycopg2.extras

my_db = psycopg2.connect(
    database="postgres",
    host="postgres",
    user="postgres",
    password="pgpass",
    port="5432",
)

app = Flask(__name__)

@app.route('/')
def home():
  print("tito")
  return render_template('index.html')


@app.route('/films', methods=['GET'])
def get_films():
    try:
        cursor = my_db.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute('SELECT * FROM films ORDER BY release_year ASC')
        films = cursor.fetchall()

        films_list = [Film(*f) for f in films]
        #for f in films:
            #films_list.append(Film(*f))

        cursor.close()

        return render_template("films.html", films=films_list)  # Retourne les films au format JSON

    except Exception as e:
        return str(e), 500  # En cas d'erreur, renvoyer une réponse d'erreur



@app.route('/film/<film>')
def film(film):
  return f"<b>{film}</b>"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)