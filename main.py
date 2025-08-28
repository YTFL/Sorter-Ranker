import sys
import os
import sorter

if __name__ == "__main__":
    raw = input("Enter items separated by commas: ")
    items = [s.strip() for s in raw.split(",") if s.strip()]

    if not items:
        print("No items provided. Exiting.")
        sys.exit(0)

    yn = input("Enable Tie/Neither options? (y/n): ").strip().lower()

    while yn not in ('y', 'n'):
        yn = input("Please enter 'y' or 'n': ").strip().lower()
    
    enable_tie_neither = (yn == 'y')

    ranked, actual, optimal, overhead, overhead_pct = sorter.interactive_rank(items, enable_tie_neither)

    # Ask if user wants to clear screen before showing results
    clear = input("Clear screen before displaying results? (y/n): ").strip().lower()
    while clear not in ('y', 'n'):
        clear = input("Please enter 'y' or 'n': ").strip().lower()

    if clear == 'y':
        os.system('cls' if os.name == 'nt' else 'clear') #cls for windows and clear for linux/mac

    print("\nFinal Ranking:")
    for idx, it in enumerate(ranked, start=1):
        print(f"{idx}. {it}")

    print(f"\nComparisons made: {actual}")
    print(f"Optimal comparisons (theoretical min): {optimal}")
    print(f"Overhead: {overhead} ({overhead_pct:.2f}%)")