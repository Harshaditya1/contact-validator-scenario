import pytest
from src.contact_validator import (
    is_valid_email,
    is_valid_phone,
    mask_email,
    normalize_phone,
)


def test_is_valid_email_true():
    """Test a well-formed email."""
    email = "student@lpu.in"

    result = is_valid_email(email)

    assert result is True


def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    phone = "555-123-4567"

    result = is_valid_phone(phone)

    assert result is True


def test_mask_email_basic():
    """Test masking a typical email address."""
    email = "priya@example.com"

    result = mask_email(email)

    # Correct expected output
    assert result == "pr***@example.com"


def test_normalize_phone():
    """Test phone normalization removes dashes."""
    phone = "555-123-4567"

    result = normalize_phone(phone)

    assert result == "5551234567"


# ---------- Extra Tests for 100% Coverage ----------

def test_is_valid_phone_type_error():
    """Non-string phone should raise TypeError."""
    with pytest.raises(TypeError):
        is_valid_phone(9876543210)


def test_mask_email_short_local():
    """2-letter local part should mask correctly."""
    assert mask_email("ab@example.com") == "a*@example.com"


def test_mask_email_invalid():
    """Invalid email should raise ValueError."""
    with pytest.raises(ValueError):
        mask_email("invalid-email")


def test_normalize_phone_invalid():
    """Invalid phone should raise ValueError."""
    with pytest.raises(ValueError):
        normalize_phone("12345")