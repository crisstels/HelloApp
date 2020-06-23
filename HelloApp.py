
from flask import request
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def calculator():
    a = request.args.get('a')
    b = request.args.get('b')
    return render_template('index.html', sum1=a, sum2=b)


if __name__ == "__main__":
    app.run(debug=True)