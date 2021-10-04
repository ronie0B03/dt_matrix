from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma =  Marshmallow(app)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')

article_schema = ArticleSchema()
# article_schema = ArticleSchema(many=True)

# @app.route('/', methods = ['GET'])
# def get_articles():
#     return jsonify({"Hello":"World"})

@app.route('/hello', methods = ['GET'])
def get_hello():
    return jsonify({"This is hello api":"World"})


@app.route('/add', methods = ['POST'])
def add_article():
    article_schema = ArticleSchema(many=False)
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)

@app.route('/', methods = ['GET'])
def get_articles():
    article_schema = ArticleSchema(many=True)
    all_articles = Articles.query.all()
    results = article_schema.dump(all_articles)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)