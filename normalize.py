import pickle

labels_filename = "labels.pickle"
sorted_paths_filename = "sorted_paths.pickle"
formatted_paths_filename = "formatted_paths_filename"
one_hot_filename = "one_hot.pickle"

with open(sorted_paths_filename, 'rb') as handle:
    paths = pickle.load(handle)

with open(labels_filename, 'rb') as handle:
    labels = pickle.load(handle)

def maxMins(data):
    vals = [[float('inf'), -float('inf')] for _ in range(6)]
    strings = ["latitude", "longitude", "speed", "altitude", "h_accuracy", "v_accuracy"]
    
    for path in data:
        for point in path:
            for i in range(6):
                if not (strings[i] != "speed" and point.get(strings[i]) == -1):
                    if point.get(strings[i]) == None:
                        point[strings[i]] = -1;
                    vals[i] = [min(vals[i][0], point.get(strings[i])), max(vals[i][1], point.get(strings[i]))]
    return vals

def normalize(data):
    vals = maxMins(data)
    print(vals)
    print("")
    strings = ["latitude", "longitude", "speed", "altitude", "h_accuracy", "v_accuracy"]
    ans = []
    for path in range(len(data)):
        ans.append([])
        for point in range(len(data[path])):
            ans[path].append([])
            for i in range(6):
                if not(data[path][point].get(strings[i]) == -1):
                    ans[path][point].append((data[path][point].get(strings[i]) - vals[i][0])/(vals[i][1] - vals[i][0]))
                else:
                    ans[path][point].append(data[path][point].get(strings[i]))
    return ans

paths = normalize(paths)

max_len = max(len(path) for path in paths)

cats = []
for label in labels:
    if label not in cats:
        cats.append(label)

one_hot = []

for label in labels:
    one_hot.append([1 if label == cats[i] else 0 for i in range(6)])

for path in paths:
    while len(path) < max_len:
        path.append([-1] * 6)

print(paths[0])
print(cats)
print(labels)
print(one_hot[0:10])


with open(formatted_paths_filename, 'wb') as handle:
    pickle.dump(paths, handle)

with open(one_hot_filename, 'wb') as handle:
    pickle.dump(one_hot, handle)

