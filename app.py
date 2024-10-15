from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
  print("tito")
  return render_template('index.html')


@app.route('/films')
def films():
  return render_template('liste.html') 

@app.route('/film/<film>')
def film(film):
  return f"<b>{film}</b>"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)
