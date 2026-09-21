from travel_data import create_record
from datetime import datetime
import json

records = [
    create_record("Chennai", "Visited Marina Beach", "05-06-2022"),
    create_record("Kochi", "Explored Fort Kochi", "15-07-2022"),
    create_record("Bangalore", "Visited Cubbon Park", "20-08-2022")
]

for record in records:
    date_object = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)

print("JSON String:")
print(json_data)

parsed_records = json.loads(json_data)

print("\nTravel Records:")

for record in parsed_records:
    print(record)