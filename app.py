from flask import Flask, render_template
import os
import pandas
app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/subnets')
def subnet():
    df = pandas.read_csv('C:\\Users\\alex\\subnet.csv')
    return render_template('table.html', csv=df)

@app.route('/vlans')
def vlans():
    df = pandas.read_csv('/Users/alexmarriott/Documents/vlans.csv')
    return render_template('vlans.html', csv=df)
if __name__ == '__main__':
    app.run(host=os.environ['FLASK_RUN_HOST'], port=os.environ['FLASK_RUN_PORT'])