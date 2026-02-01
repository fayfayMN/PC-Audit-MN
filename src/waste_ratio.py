import csv

def calculate_waste():
    total_billed = 0
    waste_billed = 0

    with open('data/pc_billing_log.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cost = float(row['pc_hours']) * float(row['pc_rate'])
            total_billed += cost
            if row['category'] in ['REDUNDANT', 'INQUIRY']:
                waste_billed += cost

    waste_percent = (waste_billed / total_billed) * 100 if total_billed > 0 else 0
    
    print(f"--- SYSTEMIC WASTE AUDIT ---")
    print(f"Total PC Fees: ${total_billed:.2f}")
    print(f"Fees spent on Redundancy/Harassment: ${waste_billed:.2f}")
    print(f"System Efficiency: {100 - waste_percent:.1f}%")
    print(f"Waste Percentage: {waste_percent:.1f}%")

if __name__ == "__main__":
    calculate_waste()
