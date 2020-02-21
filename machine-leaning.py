#File --machine-learning.py--

from sklearn import tree
import numpy as np

dataset = np.loadtxt('data.txt', delimiter=",")

features = dataset[:,1:8]
labels = dataset[:,0]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(int(clf.predict([[37,0,80,4,16,14,15]])))


# viz codes
#from sklearn.externals.six import StringIO
#import pydot

#dot_data = StringIO()

#tree.export_graphviz(clf, out_file=None, 
#        class_names=iris.labels_names,  
#        filled=True, rounded=True,  
#        special_characters=True)  
#graph = pydot.graph_from_dot_data(dot_data.getvalue())
#graph.write_pdf('test.pdf')
