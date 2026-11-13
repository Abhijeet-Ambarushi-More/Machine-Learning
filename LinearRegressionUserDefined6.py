import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of independant variables X : ",X)
    print("Values of Dependent variables Y : ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean_X is : ",mean_x)
    print("Mean_Y is : ",mean_y)

    n = len(X) #5

    numerator = 0
    denominator = 0

    # Calculate slope m :
    # m = Sum(x-xbar) * (y-ybar) / Sum(X-xbar)**2
    for i in range(n):
        numerator = numerator + ((X[i] - mean_x)*(Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)**2)

    m = numerator / denominator

    print("Slope of line m : ",m)

    # y = mx + c
    # c = y-mx
    # c = mean_y - m * mean_x

    c = mean_y - m * mean_x

    print("Y intercept C is : ",c)

    x = np.linspace(1,6,n)
    y = c + m * x

    plt.plot(x,y,color = 'g', label = "Regression line")
    plt.scatter(X,Y,color = 'r',label = "Scatter Plot")

    plt.xlabel("X : Independent variables")
    plt.ylabel("Y : Dependent variables")

    plt.legend()
    plt.show()


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()