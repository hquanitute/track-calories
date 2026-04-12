# Local Calorie Tracker

A minimal CLI tool for tracking daily calorie intake. No external dependencies — standard library only.

## Requirements

- Python 3

## Usage

### Interactive mode

Run without arguments to be prompted for each value:

```bash
python3 tracker.py        
python3 -c "from tracker import get_today_total; print(get_today_total())"
```

```
--- Local Calorie Tracker ---
Total calories consumed today: 0 kcal

Enter food name: rice
Enter weight of rice in grams: 200
How many calories are in 100g of rice? 130
Food saved to database.

Added: 200.0g of rice
Result: 260.0 calories.
New daily total: 260.0 kcal
```

### Non-interactive mode

Pass arguments directly on the command line:

```bash
python3 tracker.py <food_name> <weight_g> [cals_per_100g]
```

| Argument       | Description                                      | Required |
|----------------|--------------------------------------------------|----------|
| `food_name`    | Name of the food                                 | Yes      |
| `weight_g`     | Weight consumed in grams                         | Yes      |
| `cals_per_100g`| Calories per 100g — saves the food to database   | Only if food is not already in the database |

**Log a new food with calorie data:**

```bash
python3 tracker.py rice 200 130
```

**Log a previously saved food (no calorie data needed):**

```bash
python3 tracker.py rice 150
```

## Data Files

Two files are created automatically on first run in the working directory:

| File                | Description                                              |
|---------------------|----------------------------------------------------------|
| `food_database.json`| Maps food names to calories per 100g                    |
| `daily_log.csv`     | Append-only log of every meal with timestamp and calories|

The daily total is calculated from `daily_log.csv` each time the app runs, scoped to today's date.

## Calorie Formula

```
Total Calories = Weight (g) × (Calories per 100g ÷ 100)
```
