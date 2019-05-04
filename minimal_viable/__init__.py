"""
#Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=1000, n_features=4,n_informative=2, n_redundant=0,random_state=0, shuffle=False)
clf = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0)
clf.fit(X, y)
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=2, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=None,
            oob_score=False, random_state=0, verbose=0, warm_start=False)


"""
"""
#multilayer perceptron
from keras.models import Sequential  
from keras.layers import Dense  
from keras.layers import LSTM  
from keras.layers import Dropout  

model = Sequential()  

model.add(LSTM(units=50, return_sequences=True, input_shape=(features_set.shape[1], 1))) 
model.add(Dropout(0.2))
"""
"""
#create the confusion matrix
def createConfusion():
    import seaborn as sn
    import pandas as pd
    import matplotlib.pyplot as plt

    from sklearn.metrics import confusion_matrix
    import matplotlib.pyplot as plt

    y_true = [2, 0, 2, 2, 0, 1]
    y_pred = [0, 0, 2, 2, 0, 2]
    array = confusion_matrix(y_true, y_pred)
    size = len(array)

    df_cm = pd.DataFrame(array, range(size),
                    range(size))
    plt.figure(figsize = (10,7))
    sn.set(font_scale=1.4)#for label size
    sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size

    plt.show()

createConfusion()
"""

"""
lol = [i for i in range(10)]

with open(path + ".pkl", "wb") as f:
    pickle.dump(lol, f)

print("done")


"""

def maxMins(data):
    vals = [[float('inf'), -float('inf')] for _ in range(6)]
    strings = ["latitude", "longitude", "speed", "altitude", "h_accuracy", "v_accuracy"]
    
    for path in data:
        for point in path:
            for i in range(6):
                if not (strings[i] != "speed" and point.get(strings[i]) == -1):
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
                if not(strings[i] == "speed" and data[path][point].get(strings[i]) == -1):
                    ans[path][point].append((data[path][point].get(strings[i]) - vals[i][0])/(vals[i][1] - vals[i][0]))
                else:
                    ans[path][point].append(data[path][point].get(strings[i]))
    return ans
    

wow = {
    "latitude" : 20,
    "longitude" : 10,
    "speed" : 10,
    "altitude" : 10,
    "h_accuracy" : 10,
    "v_accuracy" : 10
}
wow2 = {
    "latitude" : 1,
    "longitude" : 1,
    "speed" : -1,
    "altitude" : 1,
    "h_accuracy" : 1,
    "v_accuracy" : 1
}
wow3 = {
    "latitude" : -1,
    "longitude" : 4,
    "speed" : 4,
    "altitude" : 4,
    "h_accuracy" : 4,
    "v_accuracy" : 4
}


data = [
     [wow],
     [wow2],
     [wow3]
]
ans = normalize(data)
print(ans)