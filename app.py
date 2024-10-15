from flask import Flask, render_template, jsonify
import os

import psycopg2

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
        cursor = my_db.cursor()

        cursor.execute('SELECT id, title, release_year FROM films')
        films = cursor.fetchall()

        films_list = []
        for film in films:
            films_list.append({
                'id': film[0],
                'title': film[1],
                'release_year': film[2]
            })

        cursor.close()

        return jsonify(films_list)  # Retourne les films au format JSON

    except Exception as e:
        return str(e), 500  # En cas d'erreur, renvoyer une réponse d'erreur



@app.route('/film/<film>')
def film(film):
  return f"<b>{film}</b>"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
