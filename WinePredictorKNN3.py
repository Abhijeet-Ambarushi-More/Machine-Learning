import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):
    border = "-"*40

    # Step 1 : Load the dataset from csv
    print(border)
    print("Step 1 : Load the dataset from CSV file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Someentries from dataset : ")
    print(df.head())
    print(border)

    # Step 2 : Clean the dataset
    print(border)
    print("Step 2 : Clean the dataset")
    print(border)

    df.dropna(inplace= True)

    print("Shape of dataset : ",df.shape)
    print("Total records : ",df.shape[0])
    print("Total columns : ",df.shape[1])

    print(border)

    # Separate independant and dependant variables

    print(border)
    print("Step 3 : Separate independant and dependant variables")
    print(border)

    X = df.drop(columns=['Class'])      # Every column except Class column
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(border)
    print("Input columns : ",X.columns.to_list())
    print("Output column : Class")
    print(border)

def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()