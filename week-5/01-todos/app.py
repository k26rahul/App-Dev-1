from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def root():
  return 'hello from root'


if __name__ == '__main__':
  app.run(debug=True)
