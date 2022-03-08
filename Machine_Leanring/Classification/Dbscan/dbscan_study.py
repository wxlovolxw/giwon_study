from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

n_sample = 2000
np.random.seed(1)

X = np.random.randn(n_sample,2)
y = np.array([0 for i in range(n_sample)])

def plot_DBSCAN(title, X, xlim, ylim):

    model = DBSCAN(eps=0.5)
    y_pred = model.fit_predict(X)

    for t in range(n_sample) :
        if model.labels_[t] == -1 :
            plt.scatter(X[t][0],X[t][1], marker='x', facecolor='b', lw=1, s=20)
        elif model.labels_[t] == 0 :
            plt.scatter(X[t][0],X[t][1], marker='o', facecolor='g', s=5)
        else : pass

    plt.grid(False)
    plt.xlim(*xlim)
    plt.ylim(*ylim)
    plt.title(title)

    return y_pred

plt.figure(figsize=(4,4))
y_pred1 = plot_DBSCAN("DBSCAN", X, (-3,3),(-3,3))
plt.show()