# https://scikit-learn.org/stable/datasets/toy_dataset.html
from sklearn.datasets import load_digits, load_diabetes
#digits = load_digits()
#x, y = digits.data, digits.target
diabetes = load_diabetes()
x, y = diabetes.data, diabetes.target
print(f"x={x.shape} y={y.shape}")
n, p = x.shape
lambda_seq = np.arange(0.0001, 20, 0.01)
#lambda_seq = np.arange(0.0001, 20, 1)
r = len(lambda_seq)
coef_seq = np.zeros((r,p))
for i in range(r):
    #coef_seq[i, :], _ = linear_lasso(x, y, lam=lambda_seq[i])
    coef_seq[i, :] = lasso2(x, y, lambda_seq[i])
    print(coef_seq[i, :])
    #break

