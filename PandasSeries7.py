import pandas as pd

def main():
    sobj = pd.Series([27000, 32000, 35000], index = ["Amit", "Sagar", "Sagar"])  

    print (sobj)

    print(sobj["Sagar"])

if __name__ == "__main__":
    main()

# if the indexes are not unique, it will print all the values with that index...so index should be unique

# indexes need to be unique like dictionary

# can not do this with normal list, only with series

# Every list is series but every series is not a list