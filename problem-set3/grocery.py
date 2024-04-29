import sys

groceries = {}

while True:
    try:
        grocery = input("Input: ").upper()

        if grocery in groceries:
            groceries[grocery] += 1
        else:
            groceries[grocery] = 1

        groceries_sorted = sorted(groceries.items(), key=lambda x:x[0])
        for k, v in groceries_sorted:
            print(f"{k}: {v}")

    except EOFError:
        print("\nThank you for coming!")
        sys.exit()