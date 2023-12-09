import numpy as np
import matplotlib.pyplot as plt


def yHat(x, w, b):
    return w*x+b


def twoPointForF(w, b):
    xAxis = [-5, 100]
    yAxis = []

    yAxis.append(w*xAxis[0]+b)
    yAxis.append(w*xAxis[1]+b)
    return [xAxis, yAxis]


def cost(xTrain, yTrain, w, b):
    m = len(xTrain)
    sigmaResult = 0
    for i in range(m):
        sigmaResult += (yHat(xTrain[i], w, b)-yTrain[i])**2

    cost = (1/(2*m))*sigmaResult

    return cost


def gradient(xTrain, yTrain, w, b):
    wGradient = 0
    bGradient = 0
    m = len(xTrain)
    for i in range(m):
        estimatedY = yHat(xTrain[i], w, b)
        wGradient += (estimatedY-yTrain[i])*xTrain[i]
        bGradient += (estimatedY-yTrain[i])

    wGradient /= m
    bGradient /= m
    return wGradient, bGradient


def gradient_descent(xTrain, yTrain, wInit, bInit, alpha, iterationNumber):
    w = wInit
    b = bInit
    for i in range(iterationNumber):
        dj_dw, dj_db = gradient(xTrain, yTrain, w, b)
        print(f"i:{i}")
        print(dj_dw)
        print(dj_db)
        w = w-(alpha*dj_dw)
        b = b-(alpha*dj_db)

    print('w:', w, 'b:', b)
    return w, b


xTrain = np.array([1., 2.])
yTrain = np.array([300., 500.])
w = 0
b = 0
alpha = 1.0e-2
iterationNumber = 10000
w, b = gradient_descent(xTrain, yTrain, w, b,
                        alpha, iterationNumber)

plt.scatter(xTrain, yTrain)
plt.plot(twoPointForF(w, b)[0], twoPointForF(w, b)[1])
plt.show()
