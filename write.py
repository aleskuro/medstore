# write.py

def save_data(filename, medicines):
    with open(filename, "w") as file:
        for med in medicines:
            line = f"{med.name},{med.brand},{med.stock}\n"
            file.write(line)