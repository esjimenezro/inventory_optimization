def economic_order_quantity(
    demand: float,
    setup_cost: float,
    holding_cost: float
) -> float:
    """
    Calculate the Economic Order Quantity (EOQ).

    Parameters
    ----------
    demand: float
        The annual demand for the product.
    setup_cost: float
        The cost incurred every time an order is placed.
    holding_cost: float
        The cost to hold one unit of the product in inventory for a year.

    Returns
    -------
    float: The optimal order quantity that minimizes total inventory costs.

    Raises
    ------
    ValueError: If any of the input parameters are non-positive.
    """
    if demand <= 0 or setup_cost <= 0 or holding_cost <= 0:
        raise ValueError("All parameters must be positive numbers.")

    eoq = (2 * demand * setup_cost / holding_cost) ** 0.5
    return eoq


def total_cost(
    demand: float,
    setup_cost: float,
    variable_transaction_cost: float,
    holding_cost: float,
    order_quantity: float,
) -> float:
    """
    Calculate the total cost of inventory management.

    Parameters
    ----------
    demand: float
        The annual demand for the product.
    setup_cost: float
        The cost incurred every time an order is placed.
    holding_cost: float
        The cost to hold one unit of the product in inventory for a year.
    order_quantity: float
        The quantity of the product ordered each time.

    Returns
    -------
    float: The total cost of inventory management.

    Raises
    ------
    ValueError: If any of the input parameters are non-positive.
    """
    if demand <= 0 or setup_cost <= 0 or holding_cost <= 0 or order_quantity <= 0:
        raise ValueError("All parameters must be positive numbers.")

    num_orders = demand / order_quantity
    holding_cost_total = (order_quantity / 2) * holding_cost
    total = (num_orders * setup_cost) + holding_cost_total + (demand * variable_transaction_cost)

    return total
