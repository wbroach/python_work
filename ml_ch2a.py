import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

from sklearn.datasets import load_breast_cancer

bcd = load_breast_cancer()

#~ for k in bcd.keys():
    #~ print(k)
    #~ if k == 'target_names':
        #~ print(bcd[k])
#~ print("Breast cancer shape: {}".format(bcd['data'].shape))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(bcd['data'], bcd['target'], random_state=0)

from sklearn.neighbors import KNeighborsClassifier

train_accuracy = []
test_accuracy = []
x_axis = range(1, 21)

for value in x_axis:
    
    knn = KNeighborsClassifier(n_neighbors=value)
    knn.fit(X_train, y_train)

    test_score = knn.score(X_test, y_test)
    train_score = knn.score(X_train, y_train)
    
    test_accuracy.append(test_score)
    train_accuracy.append(train_score)

    print("Scores for # neighbors: {}".format(value))
    print("Test set scores for {:0.2f} neighbor(s): ".format(test_score))
    print("Training set scores for {:0.2f} neighbor(s): ".format(train_score))
    print("----------------------------------------------------------------\n")

plt.plot(x_axis, train_accuracy, '-', label="Training Accuracy")
plt.plot(test_accuracy, '--', label="Test Accuracy")
plt.legend()
plt.show()
