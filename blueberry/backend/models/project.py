from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the database object
db = SQLAlchemy()

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Relationships
    projects = db.relationship('Project', backref='owner', lazy=True)
    tasks = db.relationship('Task', backref='assigned_user', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)  # Hash the password

    def check_password(self, password):
        return check_password_hash(self.password, password)  # Check password hash

    def __repr__(self):
        return f'<User {self.username}>'


# Project Model
class Project(db.Model):
    __tablename__ = 'projects'

    # Define the columns for the project table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Refers to User table
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default='Not Started')

    # Relationship with the Task model
    tasks = db.relationship('Task', backref='project', lazy=True)

    def __init__(self, name, description, owner_id, created_at=None, status='Not Started'):
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.created_at = created_at or datetime.utcnow()
        self.status = status

    def __repr__(self):
        return f'<Project {self.name}>'


# Task Model
class Task(db.Model):
    __tablename__ = 'tasks'

    # Define the columns for the task table
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)  # Refers to User table
    status = db.Column(db.String(50), default='Not Started')
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)  # Refers to Project table

    # Relationship with the User table (assigned user)
    assigned_user = db.relationship('User', backref='tasks', lazy=True)

    # Relationship with the Project table
    project = db.relationship('Project', backref='tasks', lazy=True)

    def __init__(self, task_name, due_date, assigned_to, project_id, status='Not Started'):
        self.task_name = task_name
        self.due_date = due_date
        self.assigned_to = assigned_to
        self.project_id = project_id
        self.status = status

    def __repr__(self):
        return f'<Task {self.task_name}>'
