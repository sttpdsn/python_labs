from json_csv import *
from csv_xlsx import *

if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    json_to_csv("data/samples/people_empty.json", "data/out/people_empty_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    csv_to_json("data/samples/people_empty.csv", "data/out/people_empty_from_csv.json")
    csv_to_xlsx("data/samples/cities.csv", "data/out/cities_from_csv.xlsx")
    csv_to_xlsx("data/samples/items.csv", "data/out/items_from_csv.xlsx")