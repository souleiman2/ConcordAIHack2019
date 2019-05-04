import pickle
from datetime import datetime

paths_filename = "paths.pickle"
labels_filename = "labels.pickle"
sorted_paths_filename = "sorted_paths.pickle"

with open(paths_filename, 'rb') as handle:
    paths  = pickle.load(handle)

with open(labels_filename, 'rb') as handle:
    labels = pickle.load(handle)

#2017-09-18 04:22:54UTC
def key_func(d):
    return datetime.strptime(d["timestamp"], '%Y-%m-%d %H:%M:%SUTC').timestamp()

for path in paths:
    path.sort(key=key_func)

with open(sorted_paths_filename, 'wb') as handle: 
    pickle.dump(paths, handle)
