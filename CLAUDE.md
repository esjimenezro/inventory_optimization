# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational implementation of inventory optimization concepts following a book, using Python notebooks with progressive chapters.

## Environment Setup

```bash
uv sync          # Install dependencies
```

Python 3.12 is required (see `.python-version`). Uses `uv` as the package manager.

## Running Code

```bash
python main.py                        # Run main entry point
jupyter notebook notebooks/           # Open notebooks interactively
python -c "from src.utils import *"   # Quick import check
```

No test suite or linting configuration exists in this project.

## Architecture

**`src/utils.py`** — Core utility functions shared across notebooks:
- `economic_order_quantity(demand, setup_cost, holding_cost)` — Classic EOQ formula
- `total_cost(...)` — Total inventory cost computation

**`notebooks/`** — Progressive chapter implementations:
- `chapter2`: Economic Order Quantity (EOQ) basics
- `chapter4`: Normal distribution statistics for inventory
- `chapter5`: (R, S) review policy simulation with fixed lead times
- `chapter6`: (R, S) policy with stochastic lead times
- `chapter7`: Service level optimization using `scipy.optimize`

**Key inventory concepts used:** (R, S) policy, safety stock, fill rate, cycle service level, normal loss functions. Simulations in later chapters run up to 1M iterations using NumPy for performance.

## Development Notes

- Code relevant to inventory management, forecasting, and optimization (per `.github/copilot-instructions.md`)
- Notebooks are the primary development surface; `src/utils.py` holds only reusable helpers
- Heavy use of `scipy.stats` for distribution functions and `scipy.optimize` for service level targets
