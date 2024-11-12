from flask import Flask, request, redirect, url_for, render_template
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
        cursor = callCursor()

        cursor.execute('SELECT * FROM films ORDER BY release_year ASC')
        films = cursor.fetchall()

        films_list = [Film(*f) for f in films]
        #for f in films:
            #films_list.append(Film(*f))

        cursor.close()

        return render_template("films.html", films=films_list)  # Retourne les films au format JSON

    except Exception as e:
        return str(e), 500  # En cas d'erreur, renvoyer une réponse d'erreur


def callCursor():
  return my_db.cursor(cursor_factory=psycopg2.extras.DictCursor)


@app.route('/film/<id>')
def film(id):
  try:
    cursor = callCursor()

    cursor.execute('SELECT * FROM films WHERE id = %s', (id,))
    row = cursor.fetchone()

    film = Film(row["id"], row["title"], row["release_year"], row["review"])

    cursor.close()

    return render_template("film.html", film=film)  # Retourne les films au format JSON

  except Exception as e:
    return str(e), 500  # En cas d'erreur, renvoyer une réponse d'erreur
  

@app.route('/film/form')
def getForm(): 
  return render_template("form.html")


@app.route('/film/review/<id>')
def getReviewForm(id):
    try:
      cursor = callCursor()
      
      # Retrieve the film based on the given id
      cursor.execute('SELECT * FROM films WHERE id = %s', (id,))
      row = cursor.fetchone()

      # Check if the film exists
      if row is None:
          return "Film not found", 404

      # Create a Film object to pass to the template
      film = Film(*row)

      cursor.close()

      # Pass the film object to the template
      return render_template("reviewForm.html", film=film)

    except Exception as e:
        return str(e), 500  # Return an error response if an exception occurs


@app.route('/film/add', methods=['POST'])
def addFilm():
  title = request.form.get('title')
  release_year = request.form.get('release_year')

  cursor = callCursor()

  cursor.execute('INSERT INTO films (title, release_year) VALUES (%s, %s)', (title, release_year))

  my_db.commit()
  cursor.close()

  return redirect(url_for('get_films'))

@app.route('/film/addReview/<id>', methods=['POST'])
def addReview(id):
  review = request.form.get('review')

  if not review:
    return 'passe ta review', 500 

  cursor = callCursor()

  cursor.execute('UPDATE films SET review = %s WHERE id = %s', (review, id))


  my_db.commit()
  cursor.close()

  return redirect(url_for('get_films'))

@app.route('/films/search', methods=['GET'])
def search_films():
  query = request.args.get('query', '')  # Récupérer le mot-clé de la requête
  try:
      cursor = callCursor()

      # Effectuer une requête SQL pour rechercher les films qui correspondent au mot-clé
      cursor.execute("SELECT * FROM films WHERE title ILIKE %s ORDER BY release_year ASC", ('%' + query + '%',))
      films = cursor.fetchall()

      films_list = [Film(*f) for f in films]

      cursor.close()

      return render_template("films.html", films=films_list, query=query)  # Passer les films trouvés au template

  except Exception as e:
      return str(e), 500  # Gérer les erreurs



if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)

 