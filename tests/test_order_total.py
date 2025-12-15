from orders_service import calculate_order_total
import pytest

# ========================================
# Tests: calculate_order_total
# ========================================
def test_calculate_order_total_empty():
    assert calculate_order_total([]) == 0


def test_calculate_order_total_single_item():
    items = [
        {"quantity": 2, "unit_price_cents": 1500},
    ]
    assert calculate_order_total(items) == 3000


def test_calculate_order_total_multiple_items():
    items = [
        {"quantity": 2, "unit_price_cents": 1290},
        {"quantity": 1, "unit_price_cents": 890},
        {"quantity": 3, "unit_price_cents": 500},
    ]
    # 2*1290 + 1*890 + 3*500 = 2580 + 890 + 1500 = 4970
    assert calculate_order_total(items) == 4970


def test_calculate_order_total_zero_quantity():
    items = [
        {"quantity": 0, "unit_price_cents": 1000},
    ]
    assert calculate_order_total(items) == 0