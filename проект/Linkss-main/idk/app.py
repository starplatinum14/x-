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

@app.route("/category/<category_id>")
def post_by_categories(category_id):
    categories = db.get_all_categories()
    posts = db.get_posts_by_categories(int(category_id))
    return render_template("category_post.html", categories = categories, posts = posts)

@app.route("/post/<post_id>")
def post(post_id):
    categories = db.get_all_categories()
    post = db.get_post(int(post_id))
    return render_template("post.html", categories = categories, posts = post)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)