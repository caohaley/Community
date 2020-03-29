from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import sys

app = Flask(__name__)
Bootstrap(app)

init_file = 'index.html'

if (len(sys.argv) > 1):
    init_file = sys.argv[1]

print("Starting server with " + init_file)

@app.route('/')
def index():
    return render_template(init_file)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")