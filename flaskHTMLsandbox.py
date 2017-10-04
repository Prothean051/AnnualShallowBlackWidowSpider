from flask import Flask, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key='2010749'
session['sessionTest']=request.form['No']

@app.route('/')
@app.route('/htmlExperimenting')
def htmlExperiment():
    return render_template('htmlExperimenting.html')
@app.route('/secondPage')
def secondPage():
    return render_template('secondPage.html')

if __name__ == "__main__":
    app.run(port=54321,debug=True)
