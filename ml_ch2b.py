import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn


from sklearn.datasets import load_breast_cancer

breast_cancer_database = load_breast_cancer()

print(breast_cancer_database['DESCR'])
