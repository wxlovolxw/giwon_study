import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import make_circles, make_moons
from sklearn.cluster import DBSCAN

n_samples = 1000
np.random.seed(2)
X1, y1 = make_circles(n_samples=n_samples, factor=.5, noise=.09)

# n_samples - 포인트 수
# factor - 0에서 1사이의 값. default=.8 내부원과 외부원 사이의 Scale factor
# noise - double or None의 값을 가지고, 노이즈가 가우시안 분포에 따라 데이터에 추가된다.

# Return되는 X는 생성된 샘플로 [n_samples, 2] 생성된 샘플의 좌표이다.
# y는 해당 좌표가 내부원에 속하는지(class1) 외부원에 속하는지(class0)을 알려준다.
# 예를 들어 X[y==0, 0]은 외부원에 속하는 모든 좌표들의 x좌표를 의미한다.

X2, y2 = make_moons(n_samples=n_samples, noise=.1)

def plot_DBSCAN(title, X, eps, xlim, ylim):

    # xlim과 ylim은 플랏상에 표현할 값들의 범위.
    # min_sample은 default값이 5이다. 해당 예시에서는 따로 설정하지 않았다.
    # # 주요 파라미터는 eps와 min_sample. 일정거리(eps)내에 일정갯수(min_sample)이상인 경우 핵심 샘플로 인식

    model = DBSCAN(eps=eps)
    y_pred = model.fit_predict(X)

    # 객체를 생성하고 모델을 만든다.
    # 병합군집은 predict메서드가 없고, 클러스터를 만들고 정보를 얻기 위해 fit_predict()메서드를 사용한다.

    idx_outlier = model.labels_ == -1

    # labels_ - 군집 번호를 의미한다. 아웃라이어는 -1의 값을 갖는다.

    plt.scatter(X[idx_outlier, 0], X[idx_outlier, 1], marker='x', lw=1, s=20)
    plt.scatter(X[model.labels_ == 0, 0], X[model.labels_ == 0, 1], marker='o', facecolor='g', s=5)
    plt.scatter(X[model.labels_ == 1, 0], X[model.labels_ == 1, 1], marker='s', facecolor='y', s=5)
    X_core = X[model.core_sample_indices_, :]

    # labels_에 따라서 다른 형태로 표시한다. lables_가 -1이면 x표시, 내부원이면 s, 외부원이면 o로 표시한다.

    # core_sample_indices_에는 핵심 데이터의 인덱스가 들어간다. 여기에 포함되지 않은 데이터는 경계 데이터이다.

    idx_core_0 = np.array(list(set(np.where(model.labels_ == 0)[0]).intersection(model.core_sample_indices_)))
    idx_core_1 = np.array(list(set(np.where(model.labels_ == 1)[0]).intersection(model.core_sample_indices_)))

    # np.where은 조건에 해당하는 인덱스를 찾아 준다. idx_core_0은 내부원의 좌표들을 numpy array의 형태로 저장한다.
    # .intersection()을 통해 두 리스트의 교집합을 선택한다.

    plt.scatter(X[idx_core_0, 0], X[idx_core_0, 1], marker='o', facecolor='g', s=80, alpha=0.3)
    plt.scatter(X[idx_core_1, 0], X[idx_core_1, 1], marker='s', facecolor='y', s=80, alpha=0.3)
    plt.grid(False)
    plt.xlim(*xlim)
    plt.ylim(*ylim)
    plt.xticks(())
    plt.yticks(())
    plt.title(title)
    return y_pred

plt.figure(figsize=(10, 5))
plt.subplot(121)
y_pred1 = plot_DBSCAN("Concentric-circles Clustering", X1, 0.1, (-1.2, 1.2), (-1.2, 1.2))
plt.subplot(122)
y_pred2 = plot_DBSCAN("Crecsent Clustering", X2, 0.1, (-1.5, 2.5), (-0.8, 1.2))
plt.tight_layout()
plt.show()

# 해당 예시에서는 eps는 0.1로 0.1이라는 범위 내에 5개 이상의 데이터가 존재한다면 Core_sample에 저장된다.

# 클러스터수를 따로 설정하지 않고, eps를 통해 암시적으로 통제한다.
# 데이터 스케일링 후에 eps를 설정하는 것이 좋다.

# DBSCAN의 Attributes는 다음과 같이 세가지 존재한다.
#   core_sample_indices로 core sample들의 인덱스들이다.
#   components는 트레이닝에 대한 core sample의 카피이다.
#   labels_는 데이터셋의 각 지점들에 대한 클러스터의 라벨들이다.