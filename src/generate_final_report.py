import csv

def run_audit():
    total_cost = 0
    total_labor_hours = 0
    
    print("--- GENERATING COURT AUDIT REPORT ---")
    with open('data/pc_billing_log.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cost = float(row['pc_hours']) * float(row['pc_rate'])
            labor = cost / float(row['my_hourly_pay'])
            total_cost += cost
            total_labor_hours += labor
            print(f"Date: {row['date']} | Cost: ${cost:.2f} | Required your labor: {labor:.1f} hrs")

    print("-" * 40)
    print(f"GRAND TOTAL PAID: ${total_cost:.2f}")
    print(f"TOTAL LABOR LIFE EXCHANGED: {total_labor_hours:.1f} HOURS")
    print("CONCLUSION: This represents a transfer of wealth that exceeds family stability limits.")

if __name__ == "__main__":
    run_audit()
