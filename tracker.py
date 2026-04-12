import json
import csv
import os
import sys
from datetime import datetime

# File paths
FOOD_DB_FILE = 'food_database.json'
LOG_FILE = 'daily_log.csv'

def load_food_db():
    if os.path.exists(FOOD_DB_FILE):
        with open(FOOD_DB_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_food_db(db):
    with open(FOOD_DB_FILE, 'w') as f:
        json.dump(db, f, indent=4)

def log_meal(food_name, weight, calories):
    file_exists = os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Food', 'Weight(g)', 'Calories'])
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([timestamp, food_name, weight, round(calories, 2)])

def get_today_total():
    if not os.path.exists(LOG_FILE):
        return 0
    today = datetime.now().strftime('%Y-%m-%d')
    total = 0
    with open(LOG_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Timestamp'].startswith(today):
                total += float(row['Calories'])
    return round(total, 2)

def main():
    food_db = load_food_db()

    print("--- Local Calorie Tracker ---")
    print(f"Total calories consumed today: {get_today_total()} kcal\n")

    # CLI mode: python3 tracker.py <food_name> <weight> [cals_per_100g]
    if len(sys.argv) >= 3:
        food_name = sys.argv[1].strip().lower()
        try:
            weight = float(sys.argv[2])
        except ValueError:
            print("Invalid weight. Please enter a number.")
            return
        if len(sys.argv) >= 4:
            try:
                cals_per_100g = float(sys.argv[3])
                food_db[food_name] = cals_per_100g
                save_food_db(food_db)
            except ValueError:
                print("Invalid calorie data. Please enter a number.")
                return
        elif food_name in food_db:
            cals_per_100g = food_db[food_name]
        else:
            print(f"'{food_name}' is not in your database. Provide cals_per_100g as a third argument.")
            return
    else:
        food_name = input("Enter food name: ").strip().lower()

        try:
            weight = float(input(f"Enter weight of {food_name} in grams: "))
        except ValueError:
            print("Invalid weight. Please enter a number.")
            return

        # Check if food exists in database
        if food_name in food_db:
            cals_per_100g = food_db[food_name]
        else:
            print(f"'{food_name}' is not in your database.")
            try:
                cals_per_100g = float(input(f"How many calories are in 100g of {food_name}? "))
                food_db[food_name] = cals_per_100g
                save_food_db(food_db)
                print("Food saved to database.")
            except ValueError:
                print("Invalid input. Calorie data must be a number.")
                return

    # Calculation logic
    # Total Calories = Weight * (Calories per 100g / 100)
    total_calories = weight * (cals_per_100g / 100)
    
    log_meal(food_name, weight, total_calories)
    
    print(f"\nAdded: {weight}g of {food_name}")
    print(f"Result: {round(total_calories, 2)} calories.")
    print(f"New daily total: {get_today_total()} kcal")

if __name__ == "__main__":
    main()