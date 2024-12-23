import json
from flask import Flask, request
app = Flask(__name__)


@app.route("/api/courses/<val>")
def home(val):
  alien_data = json.loads(request.data)
  return f'the course is {val}, and extra `val` is {request.args['val']}, some `xyz` is {request.args['xyz']}, also: alien data `val` is {alien_data['val']}'


if __name__ == "__main__":
  app.run(debug=True)
