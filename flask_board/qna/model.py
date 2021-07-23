from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'qna'

    id = db.Column('post_id', db.Integer, primary_key=True)
    title = db.Column(db.String(32))
    body = db.Column(db.String(100))
    author = db.Column(db.String(20))
    date = db.Column(db.String(20))
    count = db.Column(db.Integer)
    status = db.Column(db.Integer)
    attachment = db.Column(db.String(128))

    def __init__(self, title, body, author, date, count, status, attachment ):
        self.title = title
        self.body = body
        self.author = author
        # self.date = date
        # self.count = count
        # self.status = status
        # self.attachment = attachment
