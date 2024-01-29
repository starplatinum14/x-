from flask import Flask, render_template, request
import database

app = Flask(__name__)

@app.route('/')
def index():
    articles = database.get_all_articles()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = database.get_article_by_id(article_id)
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True)