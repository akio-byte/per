"""Tests for the main module."""

import pytest
from src.main import hello


def test_hello():
    """Test the hello function returns expected greeting."""
    result = hello()
    assert result == "Hello, World!"
    assert isinstance(result, str)


def test_example():
    """Basic example test to verify pytest is working."""
    assert 1 + 1 == 2


def test_hello_not_empty():
    """Test that hello function returns a non-empty string."""
    result = hello()
    assert len(result) > 0
    assert result.strip() != ""