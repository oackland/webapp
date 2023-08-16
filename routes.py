from flask import render_template, redirect, url_for
import app
from forms import StudentForm


@app.route('/')
def index():
	return render_template('home.html')


@app.route('/login')
def login():
	return render_template('login.html')


@app.route('/students', methods=['GET', 'POST'])
def add_student():
	form = StudentForm()

	if form.validate_on_submit():
		# Process form data and save to database
		# Example: student = Student(name=form.name.data, age=form.age.data)
		# Example: db.session.add(student)
		# Example: db.session.commit()
		return redirect(url_for('students'))

	return render_template('students.html', form=form)


@app.route('/about')
def about():
	return render_template('about.html')
