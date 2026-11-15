import numpy as np
import pandas as pd
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# Step 1 : Load data

#------------------------------------------------------------------
#   Function Name : LoadData
#   Description :   Load the data from CSV
#   Input :         Name of csv file
#   Output :        Data frame
#   Author :        Abhijeet Ambarushi More
#   Date :          16/08/2026
#------------------------------------------------------------------
def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset loaded successfully")
    print(df.head())

    return df

# Step 2 : Data preprocessing

#------------------------------------------------------------------
#   Function Name : PreprocessData
#   Description :   It performs data analysis
#   Input :         Data frame
#   Output :        Updated Data frame
#   Author :        Abhijeet Ambarushi More
#   Date :          16/08/2026
#------------------------------------------------------------------
def PreprocessData(df):
    df = df.drop([
        "Passengerid",
        "zero",
        "name"
    ],
    errors="ignore")

    # Handle missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())

    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert categorical to numeric
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )

    print(df.head())

    print("Data preprocessing completed")

    return df

# Step 3 : Split the data

#------------------------------------------------------------------
#   Function Name : SplitData
#   Description :   It performs spliting activity
#   Input :         Data frame
#   Output :        4 subset for training and testing
#   Author :        Abhijeet Ambarushi More
#   Date :          16/08/2026
#------------------------------------------------------------------
def SplitData(df):
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("Dataset spliting completed successfully")
    return X_train, X_test, Y_train, Y_test

# Step 4 : Train the model

#------------------------------------------------------------------
#   Function Name : TrainModel
#   Description :   It performs model training
#   Input :         Training features and labels
#   Output :        Trained model
#   Author :        Abhijeet Ambarushi More
#   Date :          16/08/2026
#------------------------------------------------------------------
def TrainModel(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)       # 1000 vela look firvayacha

    model = model.fit(X_train, Y_train)

    print("Model trained successfully")

    return model

# Step 5 : Evaluate model

#------------------------------------------------------------------
#   Function Name : EvaluateModel
#   Description :   It performs model testing
#   Input :         model, testing data(features and labels)
#   Output :        None
#   Author :        Abhijeet Ambarushi More
#   Date :          16/08/2026
#------------------------------------------------------------------
def EvaluateModel(model, X_test, Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy is : ",accuracy)

    print(confusion_matrix(Y_test, Y_pred))

#------------------------------------------------------------------
#   Function Name : main
#   Description :   Entry point function
#   Input :         None
#   Output :        None
#   Author :        Abhijeet Ambarushi More
#   Date :          16/08/2026
#------------------------------------------------------------------
def main():
    # Step 1 
    df =LoadData("MarvellousTitanicDataset.csv")

    # Step 2
    df = PreprocessData(df)

    # Step 3
    X_train, X_test, Y_train, Y_test = SplitData(df)

    # Step 4
    model = TrainModel(X_train, Y_train)

    # step 5
    EvaluateModel(model,X_test,Y_test)


if __name__ == "__main__":
    main()