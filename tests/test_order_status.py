import pytest
from orders_service import validate_order_status_transition


# ========================================
# Tests: validate_order_status_transition
# ========================================

@pytest.mark.parametrize(
    "current_status,new_status",
    [
        ("CREATED", "PAID"),
        ("CREATED", "CANCELLED"),
        ("PAID", "PREPARING"),
        ("PAID", "CANCELLED"),
        ("PREPARING", "READY"),
        ("READY", "COMPLETED"),
    ]
)
def test_valid_status_transitions(current_status, new_status):
    # Ne doit PAS lever d'exception
    validate_order_status_transition(current_status, new_status)


@pytest.mark.parametrize(
    "current_status,new_status",
    [
        ("CREATED", "READY"),
        ("PAID", "COMPLETED"),
        ("READY", "PAID"),
        ("COMPLETED", "PAID"),
        ("CANCELLED", "CREATED"),
    ]
)
def test_invalid_status_transitions(current_status, new_status):
    with pytest.raises(ValueError):
        validate_order_status_transition(current_status, new_status)






def test_unknown_current_status():
    with pytest.raises(ValueError):
        validate_order_status_transition("UNKNOWN", "PAID")