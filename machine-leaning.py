#File --machine-learning.py--

from sklearn import tree
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.wrappers.scikit_learn import KerasClassifier
#from sklearn.model_selection import StratifiedKFold
#from sklearn.model_selection import cross_val_score
import numpy as np

# Function to create model, required for KerasClassifier
#def create_model(optimizer='rmsprop', init='glorot_uniform'):
	# create model
#	model = Sequential()
#	model.add(Dense(12, input_dim=8, activation='relu'))
#	model.add(Dense(8, activation='relu'))
#	model.add(Dense(1, activation='sigmoid'))
	# Compile model
#	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#	return model

# fix random seed for reproducibility
#seed = 7
#numpy.random.seed(seed)



dataset = np.loadtxt('data.txt', delimiter=",")

X = dataset[:,1:5]
y = dataset[:,0]

#X = preprocessing.normalize(X, norm='l2')
#y = preprocessing.normalize(y, norm='l2')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .1)

#model = KerasClassifier(build_fn=create_model, verbose=0)



 # Decision Tree

#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(X_train, y_train)

# Neural Network

#clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
#    hidden_layer_sizes=(20, 10), random_state=1)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
    hidden_layer_sizes=(25,), random_state=1)

clf.fit(X_train, y_train)

prediction = clf.predict(X_test)
print(accuracy_score(y_test, prediction))

