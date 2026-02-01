def calculate_labor_cost(hourly_wage, pc_hourly_rate):
    # How many hours you have to work to pay for 1 hour of PC
    hours_needed = pc_hourly_rate / hourly_wage

    print(f"--- Labor Impact Audit ---")
    print(f"PC Hourly Rate: ${pc_hourly_rate}")
    print(f"Your Hourly Wage: ${hourly_wage}")
    print(f"Impact: You must work {hours_needed:.1f} hours to pay for 1 PC hour.")

    if hours_needed > 5:
        print("CONCLUSION: This fee structure is unsustainable for a single-income household.")

# Example: $25/hr mail carrier vs $300/hr PC
calculate_labor_cost(25, 300)
