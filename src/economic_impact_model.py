def analyze_economic_burden(mom_income, dad_income, pc_bill):
    dad_monthly = dad_income / 12
    
    # 50/50 Split Calculation
    share_cost = pc_bill / 2
    
    mom_burden_percent = (share_cost / mom_monthly) * 100
    dad_burden_percent = (share_cost / dad_monthly) * 100
    
    print(f"--- Audit Report for PC Bill: ${pc_bill} ---")
    print(f"Mom Burden: {mom_burden_percent:.1f}% of monthly income.")
    print(f"Dad Burden: {dad_burden_percent:.1f}% of monthly income.")
    
    if mom_burden_percent > 10:
        print("CRITICAL: This fee structure causes 'Financial Strangulation' for the lower earner.")

# Example: $50k vs $150k on a $1500 bill
analyze_economic_burden(50000, 150000, 1500)
