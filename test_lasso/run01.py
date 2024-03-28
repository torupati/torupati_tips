import copy
import numpy as np

np.random.seed(0)

# lasso
# https://minatosato.com/2017/10/lasso/

def soft_th(lam, x):
    return np.sign(x) * np.maximum(np.abs(x) - lam, np.zeros(1))

def centralize(X0, y0, standarized:bool=True):
    X = copy.copy(X0)
    y = copy.copy(y0)
    n, p = X.shape
    X_bar, X_sd = np.zeros(p), np.zeros(p) # mean and stdev.
    for j in range(p):
        X_bar[j] = np.mean(X[:,j])
        X_sd[j] = np.std(X[:, j])
        X[:, j] = X[:, j] - X_bar[j]
        if standarized:
            X[:, j] = X[:, j] / X_sd[j]
    if np.ndim(y) == 2:
        K = y.shape[1]
        y_bar = np.zeros(K)
        for k in range(K):
            y_bar[k] = np.mean(y[:, k])
            y[:, k] = y[:, k] - y_bar[k]
    else:
        y_bar = np.mean(y)
        y = y - y_bar
    return X, y, X_bar, X_sd, y_bar

def linear_lasso(X, y, lam, beta=None):
    n, p = X.shape
#    print(f"X({X.shape}) y({y.shape})")
    if beta is None: 
        beta = np.zeros(p)
    X, y, X_bar, X_sd, y_bar = centralize(X, y)
#    print(X_bar)
#    print(X_sd)
#    print(y_bar)
#    input()
    eps = 1
    beta_old = copy.copy(beta)
    counter = 0
    while eps > 0.00001:
        #print(f'counter={counter} eps={eps}')
        for j in range(p):
            r = y
            for k in range(p):
                if j != k:
                    #print(f"j={j} k={k}")
                    r = r - X[:, k] * beta[k]
            z = (np.dot(r, X[:, j]) / n) / (np.dot(X[:, j], X[:, j]) / n)
            print(z)
            beta[j] = soft_th(lam, z)
            input()
        eps = np.linalg.norm(beta - beta_old, 2)
        beta_old = copy.copy(beta)
    #beta = beta / X_sd
    beta_0 = y_bar - np.dot(X_bar, beta)
    return beta, beta_0

def lasso2(X, y, r):
    n = X.shape[0]
    d = X.shape[1]
    w = np.zeros(d)
    #r = 1.0
    X, y, X_bar, X_sd, y_bar = centralize(X, y)

    for _ in range(1000) :
        w[0] = (y - np.dot(X[:,1:],w[1:])).sum() / n
        for k in range(1,d) :
            w[k] = 0
            a = np.dot((y - np.dot(X, w)),X[:,k]).sum()
            b = (X[:,k] ** 2).sum()
            w[k] = (np.sign(a) * np.maximum(abs(a) - n * r, 0)) / b
        #print(w)
    return w

D = 10
M = 3
x = np.array([1, 2, -5])
A = np.array([
    [1.1, 2.3, 1.5, 2.9, 1.1, 0.2, 0.1, 2.1, 1.4, 2.2],
    [-0.5, 3, 2, 8, 3, -6, 5, 4, -2, 2],
    [-0.5, 0.3, 2.2, 8.3, 2.3, -3.6, 5.4, 4.2, -2.1, 1.2],
]).T
print(x.shape, A.shape)
y = np.dot(A, x) + np.random.randn(D)
print(f"y={y}")
print(f"y={x}")

for r in np.arange(0.0, 5.0, 0.1):
    w = lasso2(A, y, r)
    print(f"w={w}")
#w = lasso2(A, y, 1000.0)
print(f"y={x}")
