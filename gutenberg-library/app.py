from flask import Flask, render_template, request
from functools import lru_cache
import requests

app = Flask(__name__)


@lru_cache
def get_json(url):
  return requests.get(url).json()


@app.route('/')
def index():
  """ example url: /?page=2 """
  page = int(request.args.get('page', 1))
  data = get_json(f'https://gutendex.com/books/?page={page}')
  return render_template('index.html', data=data, page=page)


@app.route('/search')
def search():
  author = request.args.get('author')
  title = request.args.get('title')
  data = get_json(f'https://gutendex.com/books?search={author} {title}')
  return render_template('search.html', author=author, title=title, data=data)


if __name__ == "__main__":
  app.run(debug=True)
