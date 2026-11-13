import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousRegression(Datapath):
    Border = "-"*40

    # Step 1 : load the data
    print(Border)
    print("Step 1 : load the data")
    print(Border)

    df =pd.read_csv(Datapath)

    print(df.head())

    # Step 2 : Remove unwanted columns
    print(Border)
    print("Step 2 : Remove unwanted columns")
    print(Border)

    if"Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    # Step 3 : Check missing values
    print(Border)
    print("Step 3 : Check missing values")
    print(Border)

    print("Total missing values : ")
    print(Border)
    print(df.isnull().sum())
    print(Border)
    #  df.isnull().sum is called canonical function call
    # eka function madhun dusra function la call

    # Step 4 : Statistical summary
    print(Border)
    print("Step 4 : Statistical summary")
    print(Border)

    print(df.describe())

    # Step 5 : Correlation
    print(Border)
    print("Step 5 : Correlation")
    print(Border)

    print(df.corr())

    

    # Step 6 : Separate independent and dependent variables
    print(Border)
    print("Step 6 : Separate independent and dependent variables")
    print(Border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independant variables : ")
    print(X.head())

    print("Dependant variables : ")
    print(Y.head())

    # Step 7 : split the dataset
    print(Border)
    print("Step 7 : split the dataset")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training data: ",X_train.shape)
    print("Testing data: ",X_test.shape)

def main():
    MarvellousRegression("Advertising.csv")

if __name__ == "__main__":
    main()