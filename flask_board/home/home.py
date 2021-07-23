"""General page routes."""
from flask import Blueprint
from flask import Flask,  url_for
from flask import current_app as app
from flask import render_template
import operator

# Blueprint Configuration
home_bp = Blueprint(
    "home_bp", __name__, template_folder="templates", static_folder="static"
)



@app.route("/site-map")
def site_map():
    'Display registered routes'
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '{:25s} {:25s} {}'.format(endpoint, methods, rule)
        print(route)

    return render_template("all_links.html", rules=rules)


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

