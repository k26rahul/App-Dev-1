from flask import Flask, request, render_template, redirect

app = Flask(__name__)

""" model """
mood_data = {
    'happy': 0,
    'sad': 0
}


@app.route('/')
def index():
  return render_template('index.html', mood_data=mood_data)


@app.route('/track', methods=['POST'])
def track():
  mood = request.form['mood']
  mood_data[mood] += 1
  return redirect('/')


if __name__ == '__main__':
  app.run(debug=True)
