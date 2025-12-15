ALLOWED_STATUS_TRANSITIONS = {
    "CREATED": {"PAID", "CANCELLED"},
    "PAID": {"PREPARING", "CANCELLED"},
    "PREPARING": {"READY"},
    "READY": {"COMPLETED"},
    "COMPLETED": set(),
    "CANCELLED": set(),
}

# ========================================
# Order Status
# ========================================
def validate_order_status_transition(
    current_status: str,
    new_status: str
) -> None:
    """
    Valide une transition de statut de commande.

    Lève ValueError si la transition est invalide.
    """
    if current_status not in ALLOWED_STATUS_TRANSITIONS:
        raise ValueError(f"Statut actuel inconnu: {current_status}")

    allowed = ALLOWED_STATUS_TRANSITIONS[current_status]

    if new_status not in allowed:
        raise ValueError(
            f"Transition invalide: {current_status} → {new_status}"
        )

# ========================================
# Order Total
# ========================================
def calculate_order_total(order_items: list[dict]) -> int:
    """
    Calcule le total d'une commande en cents.

    order_items: liste de dicts contenant
      - quantity (int)
      - unit_price_cents (int)

    Retourne: total_cents (int)
    """
    if not order_items:
        return 0

    total = 0
    for item in order_items:
        qty = item["quantity"]
        price = item["unit_price_cents"]
        total += qty * price

    return total