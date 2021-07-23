"""Routes for logged-in profile."""
from pathlib import Path
import os

from flask import Blueprint, render_template, request
import requests
from flask import flash, redirect, url_for
import sqlite3
import datetime
from flask_sqlalchemy import SQLAlchemy
from .model import Post

# Blueprint Configuration
qna_bp = Blueprint(
    "qna_bp", __name__, template_folder="templates", static_folder="static", url_prefix='/qna'
)

cwd = os.getcwd()
path = Path(cwd)
project_path = path.parent
DB_PATH = str(project_path)+'/my.db'

db = SQLAlchemy()

@qna_bp.route("/read", methods=["GET"])
def read():
    """read QnA Page."""
    board1 = {
        "no": 1,
        "title": "제목이지",
        "author": "관리자",
        "date": "2021-06-18",
        "count": "224",
        "status": "공개",
        "attachment": "file-url"
    }

    board2 = {
        "no": 2,
        "title": "제목이당",
        "author": "홍길동",
        "date": "2021-06-18",
        "count": "124",
        "status": "공개",
        "attachment": "file-url"
    }

    boards = [board1, board2]


    result = {
        "boards": boards
    }

    return render_template(
        "qna_board.jinja2",
        title="ana_boad.jinja",
        template="about-template",
        result=result,
    )


@qna_bp.route("/create", methods=["POST"])
def post():
    '''
    self.title = title
    self.body = body
    self.author = author
    self.date = date
    self.count = count
    self.status = status
    self.attachment = attachment
    '''
    if request.method == 'POST':
        if not request.form['title'] or not request.form['body'] or not request.form['author']:
            flash('Please enter all the fields', 'error')
        else:
            post = Post(request.form['title'], request.form['body'],
                               request.form['author'], request.form['attachment'])

            db.session.add(post)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('test.html')
    # if request.method == 'POST':
    #     print("req: {}".format(request.form))
    #     title = request.form['title']
    #     body = request.form['body']
    #     author = request.form['author']
    #     error = None
    #     now = datetime.datetime.now()
    #     date_time = now.strftime("%Y년%m월%d일%H시%M분")
    #
    #     if request.form['attachment'] is None:
    #         attachment = ''
    #     else:
    #         attachment = request.form['attachment']
    #
    #     if not title:
    #         error = "Title is required"
    #
    #     if error is not None:
    #         flash(error)
    #     else:
    #         try:
    #             with sqlite3.connect(DB_PATH) as conn:
    #                 cur = conn.cursor()
    #                 sql ="INSERT INTO QNA(title, body, author, date, count, attachment) VALUES('"+title+"','"+body+"','"+author+"','"+str(date_time)+"','"+str(0)+"','"+attachment+"')"
    #                 print(sql)
    #                 cur.execute(sql)
    #                 conn.commit()
    #                 msg = "record success"
    #         except Exception as e:
    #             conn.rollback()
    #             print(e)
    #             msg = "insert error"
    #         finally:
    #             conn.close()
    #             print(msg)
    #             return render_template('test.html')
    # return ''