from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('ytac.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/submission')
def submission():
    return render_template('submission.html')


if __name__ == '__main__':
    app.run(debug=True)