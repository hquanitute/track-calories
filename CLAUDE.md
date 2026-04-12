# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Application

```bash
python tracker.py
```

### Show today's total calories

```bash
python3 -c "from tracker import get_today_total; print(get_today_total())"
```

### Log a meal (non-interactive)

```bash
# New food (saves calorie density to database)
python3 tracker.py rice 200 130

# Previously saved food
python3 tracker.py rice 150
```

## Architecture

This is a single-file CLI calorie tracker (`tracker.py`). It persists data in two files created at runtime:

- `food_database.json` — maps food names (lowercase strings) to calories-per-100g (float)
- `daily_log.csv` — append-only log with columns: `Timestamp`, `Food`, `Weight(g)`, `Calories`

**Data flow:** On launch, today's total is computed from the CSV. The user inputs a food name and weight. If the food isn't in the JSON database, the user is prompted for its calorie density, which is saved for future use. Calories are calculated as `weight * (cals_per_100g / 100)` and appended to the CSV.

No external dependencies — standard library only (`json`, `csv`, `os`, `datetime`).
