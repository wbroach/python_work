import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn


from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print("cancer.target_names: \n{}".format(cancer.target_names))

mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

X, y = mglearn.datasets.make_forge()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = KNeighborsClassifier(n_neighbors=3)

clf.fit(X_train, y_train)

print(clf.score(X_test, y_test))
