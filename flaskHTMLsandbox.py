from flask import Flask, url_for, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/htmlExperimenting')
def htmlExperiment():
    return render_template('htmlExperimenting.html')

if __name__ == "__main__":
    app.run(port=54321,debug=True)
