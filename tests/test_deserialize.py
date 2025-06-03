"""
Tests for service initialization
"""

import pytest
from service.models import Product, DataValidationError


def test_deserialize_invalid_boolean():
    """Test that ... does something specific."""
    data = {
        "name": "Test",
        "description": "Desc",
        "price": "10.99",
        "available": "yes",  # invalid
        "category": "FOOD",
    }
    product = Product()
    with pytest.raises(DataValidationError):
        product.deserialize(data)


def test_deserialize_missing_fields():
    """Test that ... does something specific."""
    product = Product()
    with pytest.raises(DataValidationError):
        product.deserialize({"name": "Missing everything else"})


def test_deserialize_invalid_category():
    """Test that ... does something specific."""
    data = {
        "name": "X",
        "description": "Y",
        "price": "5.00",
        "available": True,
        "category": "INVALID",
    }
    product = Product()
    with pytest.raises(DataValidationError):
        product.deserialize(data)
