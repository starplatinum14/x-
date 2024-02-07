from flask import Flask, render_template
from sql_queries import BlogDB

app = Flask(__name__)

db = BlogDB("main.db")

@app.route("/")
def index():
    categories = db.get_all_categories()
    posts = db.get_all_posts()
    print(posts)
    return render_template('index.html', title = "Hello", posts = posts, categories = categories)

@app.route("/logika")
def hello_logika():
    categories = db.get_all_categories()
    return render_template("logika1.html", categories = categories)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)