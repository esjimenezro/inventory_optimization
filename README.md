# Inventory Optimization

A Python project implementing classical and stochastic inventory management models, following an inventory optimization book chapter by chapter.

## Topics Covered

| Notebook | Topic |
|----------|-------|
| `chapter2` | Economic Order Quantity (EOQ) |
| `chapter4` | Normal distribution applied to demand modeling |
| `chapter5` | (R, S) review policy with fixed lead times |
| `chapter6` | (R, S) review policy with stochastic lead times |
| `chapter7` | Service level optimization (fill rate, safety stock) |

## Getting Started

**Install dependencies** (requires Python 3.12 and [`uv`](https://github.com/astral-sh/uv)):

```bash
uv sync
```

**Launch notebooks:**

```bash
jupyter notebook notebooks/
```

## Project Structure

```
src/utils.py        # Shared utility functions (EOQ, total cost)
notebooks/          # Chapter notebooks with theory, code, and outputs
```

### Key functions in `src/utils.py`

- `economic_order_quantity(demand, setup_cost, holding_cost)` — computes optimal order quantity minimizing total cost: `EOQ = sqrt(2DS/H)`
- `total_cost(demand, setup_cost, variable_transaction_cost, holding_cost, order_quantity)` — computes total annual inventory cost

## Dependencies

- `numpy`, `pandas` — data handling and simulation
- `scipy` — statistical distributions and optimization
- `matplotlib` — visualization
- `ipykernel` — Jupyter notebook support
