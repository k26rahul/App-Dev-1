from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/search')
def search_results():
  what_to_search = request.args.get('what_to_search')
  how_many_results = request.args.get('how_many_results')

  # url for wikipedia search API 👇
  url = f'https://en.wikipedia.org/w/rest.php/v1/search/page?q={what_to_search}&limit={how_many_results}'
  response = requests.get(url)
  data = response.json()
  return render_template('search_results.html', data=data)


if __name__ == '__main__':
  app.run(debug=True)
