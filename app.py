from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"  # You can change this later to render an HTML page

if __name__ == '__main__':
    app.run(debug=True)

