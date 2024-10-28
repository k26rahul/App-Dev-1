from flask import Flask, request, render_template
import sys

print(f'💪💪💪{len(sys.argv)=}')


def create_path():
  if len(sys.argv) < 2:
    return '/static'
  else:
    return f'/{sys.argv[1]}'


app = Flask(__name__, static_url_path=create_path())


@app.route('/')
def root():
  return 'good eve Vidu 🌟'


if __name__ == "__main__":
  print('😱 app.static_url_path = ', app.static_url_path)
  print('😱 app.static_folder = ', app.static_folder)
  app.run(debug=True)
