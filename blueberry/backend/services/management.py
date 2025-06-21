from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from backend.models.project import Project, Task, db
from backend.models.user import User
from werkzeug.security import check_password_hash
from datetime import date

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management

# Route to render the management page for managing and storing data


@app.route('/')
def management():
    if 'user_id' not in session:
        flash("You need to log in to access the management page!", "danger")
        return redirect(url_for('login'))

    projects = Project.query.filter_by(owner_id=session['user_id']).all()  # Get all projects for the logged-in user
    current_date = date.today().strftime("%Y-%m-%d")  # Get today's date in the format YYYY-MM-DD
    return render_template('management.html', projects=projects, current_date=current_date)


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
        return redirect(url_for('management'))


# Route to handle project deletion
@app.route('/projects/delete/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash("Project deleted successfully!", "success")
    return redirect(url_for('management'))


# Route to handle editing a project
@app.route('/projects/edit/<int:project_id>', methods=['GET', 'POST'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        project.name = request.form['project_name']
        project.description = request.form['project_description']
        project.status = request.form['status']
        db.session.commit()
        return redirect(url_for('management'))  # Redirect to management page after editing
    return render_template('edit_project.html', project=project)


# User Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find user by email
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):  # Check the password
            session['user_id'] = user.id  # Store user id in session
            flash("Login successful!", "success")
            return redirect(url_for('management'))
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
