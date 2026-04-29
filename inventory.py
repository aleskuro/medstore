# DISPLAY (TABLE FORMAT)
def display_medicines(data):
    print("\n------ Available Medicines --------\n")

    # Table Header
    print(f"{'S.N.':<5}{'Name':<25}{'Brand':<20}{'Stock':<10}")
    print("-" * 60)

    # Table Rows
    for i, med in enumerate(data, 1):
        print(f"{i:<5}{med['name']:<25}{med['brand']:<20}{med['stock']:<10}")