import flask 
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config.from_object(__name__) 

@app.route('/home')
@app.route('/')
def index(): 
	return render_template('home.html') # tasks = tasks)

@app.route('/query', methods=['POST'])
def query():
	if request.method == 'POST':
		userinput ={ mealtype : request.form.get("mealtype", None),
		price : request.form.get("price", None)
		transport : request.form.get("transport", None),
		distance : request.form.get("distance", None),
		ambience : request.form.get("transport", None),
		cuisine : request.form.get("cuisine", None)
		}
		return redirect(url_for('index'))
	return redirect(url_for('index'))

# Make a query in the Pyswip Library.
if __name__ == '__main__': 
	app.run(debug=True) 
