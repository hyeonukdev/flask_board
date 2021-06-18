"""General page routes."""
from flask import Blueprint
from flask import current_app as app
from flask import render_template


# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)


@home_bp.route("/", methods=["GET"])
def home():
    """Homepage."""
    return render_template(
        "index.jinja2",
        title="Flask Blueprint Demo",
        subtitle="Demonstration of Flask blueprints in action.",
        template="home-template",
    )


@home_bp.route("/about", methods=["GET"])
def about():
    """About page."""
    return render_template(
        "index.jinja2",
        title="About",
        subtitle="This is an example about page.",
        template="home-template page",
    )


@home_bp.route("/contact", methods=["GET"])
def contact():
    """Contact page."""
    return render_template(
        "index.jinja2",
        title="Contact",
        subtitle="This is an example contact page.",
        template="home-template page",
    )


@home_bp.route("/gtest", methods=["GET"])
def gtest():
    result = "ok"
    value = "test"
    return render_template('test.jinja2', result=result, value=value, )


@home_bp.route("/ptest", methods=["POST"])
def ptest():
    text = "ok"
    value = "test"
    result = {
        "text":text,
        "value":value
    }
    return result
