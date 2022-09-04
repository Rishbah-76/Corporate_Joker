from flask import Flask,request,render_template
from joke.exception import JokeException
from joke.logger import logging
import random
import pyjokes
import pandas as pd
import sys

df=pd.read_csv(r"joke\jokes_edited.csv")
l=list(df['Joke'])

app = Flask(__name__)

@app.route('/')
def index():
    try:
        logging.info("Home page opened")
        return render_template('index.html',methods=['GET','POST'],embed="")
        
    except Exception as e:
        raise JokeException(e,sys) from e

@app.route('/random_joke')
def result1():
    try:
        logging.info("joke page opened")
        k=['1','2']
        ch=random.choice(k)
        if ch=='1':
            n=pyjokes.get_joke(language='en', category='all')
        else:
            n=random.choice(l)
        return render_template('result1.html',methods=['GET'],embed=n)
    except Exception as e:
        raise JokeException(e,sys) from e

@app.route('/team')
def team():
    try:
        return render_template('team.html',methods=['GET','POST'])
    except Exception as e:
        raise JokeException(e,sys) from e

@app.route('/about')
def about():
    try:
        return render_template('about.html',methods=['GET','POST'])
    except Exception as e:
        raise JokeException(e,sys) from e


if __name__=="__main__":
    app.run(debug=True)