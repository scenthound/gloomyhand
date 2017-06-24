'''
Gloomhaven hand builder
author: Mike Lee (scenthound)
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', message="No Testa Me")

if __name__ == "__main__":
    app.run(debug=True)
