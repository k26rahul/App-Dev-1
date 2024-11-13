from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
  data = requests.get('https://poetrydb.org/author').json()
  return render_template('index.html', data=data)


@app.route('/poetry-by/<author>')
def poetry_by_author(author):
  url = f'https://poetrydb.org/author/{author}/title'
  data = requests.get(url).json()
  return render_template('poetry_by_author.html', author=author, data=data)


@app.route('/poetry-by/<author>/<title>')
def poetry_by_author_title(author, title):
  url = f'https://poetrydb.org/author,title/{author};{title}'
  data = requests.get(url).json()
  return render_template('poetry_by_author_title.html', author=author, title=title, data=data)


if __name__ == '__main__':
  app.run(debug=True)
