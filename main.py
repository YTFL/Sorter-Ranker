import os
from readFromTXT import read_items_from_txt
from enterManual import read_items_manual

def main():
    print("How would you like to input your items?")
    print("1. From a file")
    print("2. Enter manually")
    choice = input("Enter 1 or 2: ").strip()
    while choice not in ('1', '2'):
        choice = input("Please enter 1 or 2: ").strip()

    items = []
    if choice == '1':
        print("Choose file input method:")
        print("1. Scan directories automatically (not implemented)")
        print("2. Enter file path manually")
        file_choice = input("Enter 1 or 2: ").strip()
        while file_choice not in ('1', '2'):
            file_choice = input("Please enter 1 or 2: ").strip()
        if file_choice == '1':
            print("Directory scanning not implemented yet.")
            return
        else:
            file_path = input("Enter the path to your file: ").strip()
            if not file_path:
                print("No file path provided. Exiting.")
                return
            ext = os.path.splitext(file_path)[1].lower()
            if ext == '.txt':
                try:
                    items = read_items_from_txt(file_path)
                except Exception as e:
                    print(f"Error: {e}")
                    return
            elif ext == '.csv':
                print("CSV file support not implemented yet.")
                return
            elif ext in ('.xls', '.xlsx'):
                print("Excel file support not implemented yet.")
                return
            else:
                print("Unsupported file type. Only .txt, .csv, and Excel files are supported.")
                return
    else:
        items = read_items_manual()

    # Ask for tie/neither options
    yn = input("Enable Tie/Neither options? (y/n): ").strip().lower()
    while yn not in ('y', 'n'):
        yn = input("Please enter 'y' or 'n': ").strip().lower()
    enable_tie_neither = (yn == 'y')

    # Sort
    from sorter import interactive_rank
    ranked, actual, optimal, overhead, overhead_pct = interactive_rank(items, enable_tie_neither)

    # Ask if user wants to clear screen before showing results
    clear = input("Clear screen before displaying results? (y/n): ").strip().lower()
    while clear not in ('y', 'n'):
        clear = input("Please enter 'y' or 'n': ").strip().lower()
    if clear == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')

    print("\nFinal Ranking:")
    for idx, it in enumerate(ranked, start=1):
        print(f"{idx}. {it}")
    print(f"\nComparisons made: {actual}")
    print(f"Optimal comparisons (theoretical min): {optimal}")
    print(f"Overhead: {overhead} ({overhead_pct:.2f}%)")

    # Ask if user wants to save output or history
    save = input("Do you want to save the output and sorting history? (y/n): ").strip().lower()
    while save not in ('y', 'n'):
        save = input("Please enter 'y' or 'n': ").strip().lower()
    if save == 'y':
        # Placeholder for save functionality
        print("Save functionality not implemented yet.")

if __name__ == "__main__":
    main()