from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from backend.models.project import Project, db
from backend.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_name.db'  # Example for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking for performance reasons

# Initialize the SQLAlchemy instance with the app
db.init_app(app)


# Route to render the management page for managing and storing data
@app.route('/')
def management():
    if 'user_id' not in session:
        flash("You need to log in to access the management page!", "danger")
        return redirect(url_for('login'))

    projects = Project.query.filter_by(owner_id=session['user_id']).all()  # Get all projects for the logged-in user
    current_date = date.today().strftime("%Y-%m-%d")  # Get today's date in the format YYYY-MM-DD
    return render_template('management.html', projects=projects, current_date=current_date)


# Route to render the projects page
@app.route('/projects')
def projects_page():
    if 'user_id' not in session:
        flash("You need to log in to view the projects!", "danger")
        return redirect(url_for('login'))

    projects = Project.query.filter_by(owner_id=session['user_id']).all()  # Get all projects for the logged-in user
    return render_template('projects.html', projects=projects)


# Route to handle project creation
@app.route('/projects/create', methods=['POST'])
def create_project():
    if request.method == 'POST':
        name = request.form['project_name']
        description = request.form['project_description']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        estimate = request.form['project_estimate']

        # Get the owner from the session (logged-in user)
        owner_id = session.get('user_id')

        # Ensure the user is logged in
        if not owner_id:
            flash("You need to log in to create a project!", "danger")
            return redirect(url_for('login'))

        # Create a new project
        new_project = Project(
            name=name,
            description=description,
            owner_id=owner_id,  # Set the owner to the logged-in user
            created_at=datetime.utcnow(),
            status="Not Started"
        )
        db.session.add(new_project)
        db.session.commit()
        flash("Project created successfully!", "success")
        return redirect(url_for('projects_page'))


# Route to handle project deletion
@app.route('/projects/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash("Project deleted successfully!", "success")
    return redirect(url_for('projects_page'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        try:
            fullname = request.form['fullname']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']

            # Check if user already exists
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash("Email is already registered!", "danger")
                return redirect(url_for('login'))

            # Hash the password
            hashed_password = generate_password_hash(password, method='sha256')

            # Create a new user
            new_user = User(
                fullname=fullname,
                email=email,
                username=username,
                password_hash=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()

            flash("Account created successfully! Please log in.", "success")
            return redirect(url_for('login'))  # Redirect to login page
        except Exception as e:
            flash("An error occurred during signup. Please try again.", "danger")
            return redirect(url_for('signup'))

    return render_template('signup.html')


# Route to handle editing a project
@app.route('/projects/edit/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        project.name = request.form['project_name']
        project.description = request.form['project_description']
        project.status = request.form['status']
        db.session.commit()
        return redirect(url_for('projects_page'))  # Redirect to projects page after editing
    return render_template('edit_project.html', project=project)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find the user by email
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id  # Store user id in session
            flash("Login successful!", "success")
            return redirect(url_for('management'))  # Redirect to the dashboard
        else:
            flash("Invalid email or password!", "danger")

    return render_template('login.html')


# User Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove the user from the session
    flash("Logged out successfully", "info")
    return redirect(url_for('login'))


# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
