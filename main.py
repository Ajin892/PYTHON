from tripdata import get_trip
from datetime import datetime
import json

trips = [
    get_trip("Chennai", "15-05-2023", "Visited Marina Beach"),
    get_trip("Kochi", "20-06-2023", "Explored Fort Kochi"),
    get_trip("Bangalore", "10-08-2023", "Visited Cubbon Park")
]

for trip in trips:
    date_object = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_object.strftime("%B %d, %Y")

json_data = json.dumps(trips, indent=4)

print(json_data)