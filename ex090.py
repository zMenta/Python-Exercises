#Write a algorithm that reads the name and the final grade of a student ( grade > 7 is approved, < 7 failed). Then stores the situation this student is in a dictionary

record = {}

record["name"] = str(input("Please type the student name: "))
record["grade"] = float(input(f"Please type {record['name']}'s final grade: "))

if record["grade"] >= 7:
    record["status"] = "approved"
else:
    record["status"] = "failed"

for k , v in record.items():
    print(f"{k} is {v}")

