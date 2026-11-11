import pandas as pd

def main():
    sobj = pd.Series([11.2,21,"51.2",True])     # As data is heterogeneous it will print 'object' as dtype

    print(sobj)

if __name__ == "__main__":
    main()