import json
import pickle
from random import shuffle

data_dir = "../data/"
trips_path = "trips_data_1/trajets_mtl_trajet_2017-1.geojson"
points_path = "points_data/points_mtl_trajet_2017-1.geojson"

ids_dict_filename = "ids_dict.pickle"

print("loading trips...")
with open(data_dir + trips_path) as json_file:
    text = json_file.read()
    trips_struct = json.loads(text);
    print("trips loaded!")

trips_features = trips_struct["features"]
mode_dict = {}
for features in trips_features:
    properties = features["properties"]
    if "mode" in properties and ',' not in properties["mode"] and properties["mode"] not in ["ND", "Autre"]:
        mode = properties["mode"]
        if mode not in mode_dict.keys():
            mode_dict[mode] = {"count": 0, "ids": []}
        mode_dict[mode]["count"] += 1
        mode_dict[mode]["ids"].append(properties["id_trip"])

count_dict = {k : v["count"] for k,v in mode_dict.items()}
ids_dict = {k : v["ids"] for k,v in mode_dict.items()}

print(count_dict)
print({k: len(v) for k,v in ids_dict.items()})


for v in ids_dict.values():
    shuffle(v)

with open(ids_dict_filename, 'wb') as handle:
    pickle.dump(ids_dict, handle)
