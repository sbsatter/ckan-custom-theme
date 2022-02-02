"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.custom_theme.logic import validators


def test_custom_theme_reauired_with_valid_value():
    assert validators.custom_theme_required("value") == "value"


def test_custom_theme_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.custom_theme_required(None)
