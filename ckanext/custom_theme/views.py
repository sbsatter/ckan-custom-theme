from flask import Blueprint


custom_theme = Blueprint(
    "custom_theme", __name__)


def page():
    return "Hello, custom_theme!"


custom_theme.add_url_rule(
    "/custom_theme/page", view_func=page)


def get_blueprints():
    return [custom_theme]
