import pickle

labels_filename = "labels.pickle"
sorted_paths_filename = "sorted_paths.pickle"

with open(sorted_paths_filename, 'rb') as handle:
    paths  = pickle.load(handle)

with open(labels_filename, 'rb') as handle:
    labels = pickle.load(handle)

path_lengths = list(map(lambda p: len(p), paths))
max_len = max(path_lengths)



