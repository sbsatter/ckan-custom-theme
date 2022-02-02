"""Tests for helpers.py."""

import ckanext.custom_theme.helpers as helpers


def test_custom_theme_hello():
    assert helpers.custom_theme_hello() == "Hello, custom_theme!"
