from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.htm')

@app.route("/shop")
def shop():
    return render_template("flexbox-shop.htm")

@app.route("/grid")
def grid():
    return render_template("grid.htm")

if __name__ == '__main__':
    app.run(debug=True)