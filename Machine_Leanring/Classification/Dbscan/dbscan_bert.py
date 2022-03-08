from sklearn.cluster import DBSCAN
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_csv('../results-20200730-135718.csv')
n_sample = 1861

list_x = df['interest_rate'].values.tolist()
list_y = df['skip_rate'].values.tolist()

A = []
try :
    for t in range(n_sample) :
        cor = []
        cor.append(list_x[t])
        cor.append(list_y[t])

        A.append(cor)
except IndexError : pass

X = np.array(A)

def plot_DBSCAN(title, X, xlim, ylim):

    model = DBSCAN(eps=0.03)
    y_pred = model.fit_predict(X)

    try :
        for t in range(n_sample) :
            if model.labels_[t] == -1 :
                plt.scatter(X[t][0],X[t][1], marker='x', facecolor='b', lw=1, s=20)
            elif model.labels_[t] == 0 :
                plt.scatter(X[t][0],X[t][1], marker='o', facecolor='g', s=5)
            else : pass
    except IndexError : pass

    plt.grid(False)
    plt.xlim(*xlim)
    plt.ylim(*ylim)
    plt.title(title)

    return y_pred

plt.figure(figsize=(4,4))
y_pred1 = plot_DBSCAN("DBSCAN", X, (-0.1,1.1),(-0.1,1.1))
plt.show()