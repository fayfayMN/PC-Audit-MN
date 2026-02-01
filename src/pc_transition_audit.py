def audit_transitions():
    # Data: [PC_Number, Years_Active, Total_Cost, Efficiency_Rating(1-10)]
    history = [
        [1, 2, 5000, 5], 
        [2, 1.5, 8000, 3],
        [3, 1, 12000, 2],
        [4, 2, 15000, 1],
        [5, 1.5, 20000, 0]
    ]
    
    print("--- 8-YEAR MULTI-PC FINANCIAL DRAIN ---")
    total_spent = sum(row[2] for row in history)
    for pc in history:
        print(f"PC #{pc[0]}: Spent ${pc[2]:,} over {pc[1]} years.")
    
    print(f"\nTOTAL CAPITAL DRAIN: ${total_spent:,}")
    print("Finding: Costs increased by 300% as PC quality decreased.")

if __name__ == "__main__":
    audit_transitions()
