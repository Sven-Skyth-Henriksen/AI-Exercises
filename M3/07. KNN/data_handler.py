from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from knn import KNN
import matplotlib.pyplot as plt
myKNN = KNN(3)


X, Y = make_blobs(n_samples = 300, centers = 4, cluster_std = 1, random_state = 0)

print(X[0])

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

preds = myKNN.predict(x_train,x_test,y_train)

acc = myKNN.evaluate(preds, y_test)

print(acc)

