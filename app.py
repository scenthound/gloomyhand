'''
Gloomhaven hand builder
author: Mike Lee (scenthound)
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def title():
    return "Gloomhaven hand builder!"

if __name__ == '__main__':
    app.run()
