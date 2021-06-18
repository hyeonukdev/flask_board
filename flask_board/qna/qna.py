"""Routes for logged-in profile."""
from flask import Blueprint, render_template
import requests
from flask import flash, redirect, url_for

# Blueprint Configuration
qna_bp = Blueprint(
    "qna_bp", __name__, template_folder="templates", static_folder="static", url_prefix='/qna'
)


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
def create():
    if requests.method == 'POST':
        title = requests.form['title']
        body = requests.form['body']
        error = None

        if not title:
            error = "Title is required"

        if error is None:
            flash(error)
        else:
            # db에 insert
            # db.get()
            # db.execute()
            # db.commit()
            return redirect(url_for('qna_board.jinja'))

    return