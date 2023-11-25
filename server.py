from flask import Flask
from flask import render_template

app = Flask(__name__)


# Rendering an html file
# @app.route('/')
# def home_page():
#     return render_template('index.html')


@app.route('/')
def home_page():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
