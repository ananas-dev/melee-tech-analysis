#File --machine-learning.py--

from sklearn import tree
import numpy as np

dataset = np.loadtxt('test.txt', delimiter=",")

features = dataset[:,1:5]
labels = dataset[:,0]


clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(int(clf.predict([[-52,0,-43,7]])))