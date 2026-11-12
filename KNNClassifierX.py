import numpy as np
from sklearn.neighbors import KNeighborsClassifier

def main():
    # Independant
    X = np.array([
        [1,2],
        [2,3],
        [3,1],
        [5,6]
    ])

    # Dependant
    Y = np.array(["Red","Red","Blue","Blue"])

    new_point = np.array([3,3])

    print("Independent Vvariables are : ")
    print(X)

    print("Dependent Vvariables are : ")
    print(Y)

    print("Testing point is : ")
    print(new_point)

if __name__ == "__main__":
    main()