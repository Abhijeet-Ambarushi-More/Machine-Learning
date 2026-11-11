import pandas as pd

def main():
    sobj = pd.Series([11,21,51,101], index = ["C","C++","Java","Python"])  

    print (sobj)

    print(sobj["Python"])

if __name__ == "__main__":
    main()

# indexes need to be unique like dictionary

# can not do this with normal list, only with series

# Every list is series but every series is not a list