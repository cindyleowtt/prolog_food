
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import hashlib

app = Flask(__name__)
app.config.from_object(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kanban.db' 
app.config['SECRET_KEY'] = 'THISISREAL'
app.config['USERNAME'] = 'admin'
app.config['PASSWORD'] = 'pass'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
	'''SQLAlchemy class for users. 3NF Normalised.'''
	__tablename__ = 'users'
	id = db.Column('id', db.Integer, primary_key = True)
	username = db.Column('username', db.String(15))
	password = db.Column('password', db.String(15))

	def ___init__(self, username, password):
		self.username = username
		self.password = password

class Flasks(db.Model):
	'''SQLAlchemy class for each task. 3NF Normalised.'''
	__tablename__ = 'flasks'
	id = db.Column('id', db.Integer, primary_key = True)
	task = db.Column('task', db.String(200))
	state = db.Column('state', db.String(10))
	task_user = db.Column('task_user', db.String(15))

	def ___init__(self, task, state, task_user):
		self.task = task
		self.state = state
		self.task_user = task_user

	def json(self):
		return {
			'id': self.id,
			'task': self.task,
			'state': self.state,
			'task_user': self.task_user
		}
