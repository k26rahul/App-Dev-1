from flask import Flask
app = Flask(__name__)


@app.route("/greet/<string:name>")
def home(name):
  return "Hello, " + name


if __name__ == "__main__":
  app.run()
