import ckan.plugins.toolkit as tk


def custom_theme_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "custom_theme_required": custom_theme_required,
    }
