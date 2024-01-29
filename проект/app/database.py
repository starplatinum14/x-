class Database:
    def __init__(self):
        # Імітована база даних
        self.articles = [
            {'id': 1, 'title': 'Dota 2 Overview', 'content': '...'},
            {'id': 2, 'title': 'Heroes', 'content': '...'},
            # Додайте інші статті
        ]

    def get_all_articles(self):
        return self.articles

    def get_article_by_id(self, article_id):
        for article in self.articles:
            if article['id'] == article_id:
                return article
        return None

db = Database()
