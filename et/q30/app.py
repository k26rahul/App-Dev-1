from flask import Flask

app = Flask(__name__)


@app.route('/abc')
def abc():
  return 'ok'


app.run(debug=True)
