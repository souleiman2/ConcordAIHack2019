import json
import pickle

data_dir = "../data/"
trips_path = "trips_data_1/trajets_mtl_trajet_2017-1.geojson"
points_path = "points_data/points_mtl_trajet_2017-1.geojson"

ids_dict_filename = "ids_dict.pickle"
paths_filename = "paths.pickle"
labels_filename = "labels.pickle"

with open(ids_dict_filename, 'rb') as handle:
    ids_dict = pickle.load(handle)

ids_dict = {k : v[:350] for k,v in ids_dict.items()}
print({k : len(v) for k,v in ids_dict.items()})

ids = []
labels = []
for k, v in ids_dict.items():
    for id_ in v:
        ids.append(id_)
        labels.append(k)

print("loading data...")
with open(data_dir + points_path) as json_file:
    text = json_file.read()
    #json_data = text.replace('\0', '')
    struct = json.loads(text)
    print("data loaded!")

labels = []
path_dict = {x: [] for x in ids}
features = struct["features"]
for i, feature in enumerate(features):
    if i % (len(features)//1000) == 0:
        print(i/len(features))
    properties = feature["properties"]
    id_trip = properties["id_trip"]
    if id_trip in ids:
        path_dict[id_trip].append(properties.values)

print(len(path_dict))
print(len(labels))
paths = list(map(lambda x: path_dict[x], ids))
print(len(paths))

with open(paths_filename, 'wb') as handle:
    pickle.dump(paths, handle)

with open(labels_filename, 'wb') as handle:
    pickle.dump(labels, handle)

