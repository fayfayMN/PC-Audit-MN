

import csv
from datetime import datetime

def check_stability():
    dates = []
    with open('data/modification_log.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(datetime.strptime(row['date'], '%Y-%m-%d'))
    
    dates.sort()
    if len(dates) < 2:
        print("Not enough data to calculate frequency.")
        return

    # Calculate average days between "changes"
    total_days = (dates[-1] - dates[0]).days
    frequency = total_days / len(dates)
    
    print(f"--- PC STABILITY AUDIT ---")
    print(f"Total Modifications: {len(dates)}")
    print(f"Average time between changes: {frequency:.1f} days")
    
    if frequency < 30:
        print("RESULT: High Volatility. The PC is functionally rewriting the Decree.")

if __name__ == "__main__":
    check_stability()


