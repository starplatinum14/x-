
from flask import Flask, render_template
from database import Database  # Імпортуйте клас Database з файлу database.py

app = Flask(__name__)

db = Database()

@app.route('/')
def index():
    articles = db.get_all_articles()  # Використовуйте об'єкт db для виклику функцій
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = db.get_article_by_id(article_id)
    return render_template('article.html', article=article)

if __name__ == '__main__':
    app.run(debug=True)
