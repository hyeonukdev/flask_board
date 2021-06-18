"""Routes for logged-in profile."""
from flask import Blueprint, render_template

# Blueprint Configuration
about_bp = Blueprint(
    "about_bp", __name__, template_folder="templates", static_folder="static"
)


@about_bp.route("/about/guide", methods=["GET"])
def guide():
    """User Guide Page."""

    # 기능
    guide_function = "캡스톤디자인 작품 조회"

    # 세부내용
    guide_detail = "다양한 작품을 검색할 수 있습니다"

    # 예시
    guide_example = "image-url"

    result = {
        "guide_function": guide_function,
        "guide_detail": guide_detail,
        "guide_example": guide_example
    }

    return render_template(
        "about_guide.jinja2",
        title="about_guide.jinja",
        template="about-template",
        result=result,
    )


@about_bp.route("/about/background", methods=["GET"])
def background():
    """Develpoment Background Page."""

    # 배경
    background = '''
                개발배경에 관한 주절주절
                '''

    result = {
        "background":background
    }

    return render_template(
        "about_background.jinja2",
        title="about_guide.jinja",
        template="about-template",
        result=result,
    )
