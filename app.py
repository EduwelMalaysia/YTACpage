from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('ytac.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/registration/success')
def registration_success():
    return render_template('registration-success.html')


@app.route('/submission')
def submission():
    return redirect(url_for('student_portal') + '#project')

@app.route('/student')
def student_portal():
    return render_template('student.html')


@app.route('/admin')
def admin_portal():
    return render_template('admin.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
