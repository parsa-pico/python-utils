import numpy as np
from sklearn.preprocessing import StandardScaler


def yHat(x, w, b):
    return np.dot(w, x) + b


def cost(xTrain, yTrain, w, b):
    m = len(xTrain)
    sigmaResult = 0
    for i in range(m):
        sigmaResult += (yHat(xTrain[i], w, b)-yTrain[i])**2

    cost = (1/(2*m))*sigmaResult

    return cost

# i think this is wrong
# def derative(x, w, respectToWIndex):
#     derativeResult = 0
#     for i in range(w):
#         if i != respectToWIndex:
#             derativeResult += x[i]
#         else:
#             derativeResult += x[i]*w[i]
#     return derativeResult


def gradient(xTrain, yTrain, w, b):
    wGradient = np.zeros(len(w))
    bGradient = 0
    m = len(xTrain)
    n = len(w)
    estimatedY = np.zeros(m)
    for i in range(m):
        estimatedY[i] = yHat(xTrain[i], w, b)
        bGradient += estimatedY[i]-yTrain[i]
    for i in range(n):
        for j in range(m):
            # estimatedY = yHat(xTrain[j], w, b)
            wGradient[i] += (estimatedY[j]-yTrain[j])*xTrain[j][i]

    wGradient /= m
    bGradient /= m
    return wGradient, bGradient


def gradient_descent(xTrain, yTrain, wInit, bInit, alpha, iterationNumber):
    w = wInit
    b = bInit
    for i in range(iterationNumber):
        dj_dw, dj_db = gradient(xTrain, yTrain, w, b)
        w = w-(alpha*dj_dw)
        b = b-(alpha*dj_db)

    return w, b


xTrain = np.arange(0, 20, 1)

X = np.c_[xTrain, xTrain**2, xTrain**3,
          xTrain**4, xTrain**5, xTrain**6,
          xTrain**7, xTrain**8, xTrain**9, xTrain**10]

w = np.zeros((X.shape[1],))
b = 0
scalar = StandardScaler()

X = scalar.fit(X).transform(X)
# print(X)
yTrain = np.cos(xTrain/2)
alpha = 1e-1
iterationNumber = 10000
w, b = gradient_descent(X, yTrain, w, b,
                        alpha, iterationNumber)


# print('b:', b, 'w:', w, )
for i in range(X.shape[0]):
    print(np.dot(w, X[i])+b)
    print(yTrain[i])
    print('--')
