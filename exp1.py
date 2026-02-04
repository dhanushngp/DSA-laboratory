import csv
import json

# --- Writing to a text file ---
with open("data.txt", "w") as f:
    f.write("Hello DSA File Handling!\n")
    f.write("42\n")

# --- Reading from a text file ---
with open("data.txt", "r") as f:
    for line in f:
        print("Read:", line.strip())

# --- Writing to a CSV file ---
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Alice", 90])
    writer.writerow(["Bob", 85])

# --- Reading from a CSV file ---
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], "scored", row["Score"])

# --- Writing to a JSON file ---
data = {"students": [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 85}]}
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

# --- Reading from a JSON file ---
with open("data.json", "r") as f:
    parsed = json.load(f)
    for student in parsed["students"]:
        print(student["name"], "scored", student["score"])

print("good")
print("hey")