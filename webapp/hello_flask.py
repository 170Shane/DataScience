from flask import Flask

app = Flask(__name__)


@app.route('/<string:name>')
def hello(name) -> str:
    return 'Hello World from ' + name

@app.route('/a')
def hello() -> str:
    return 'Hello World from Flask new version'

if __name__=="__main__":
    app.run(debug=True)

# app.run()
