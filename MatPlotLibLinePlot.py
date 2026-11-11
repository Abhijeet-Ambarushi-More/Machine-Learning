import matplotlib.pyplot as plt

def main():
    X = [1, 2, 3, 4, 5]
    Y = [10, 25, 18, 35, 30]

    plt.plot(
        X ,
        Y,
        marker = "o",
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )

    plt.title("Marvellous Line Plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.grid(True)

    plt.legend()    # nav distat sagla che

    plt.show()  # ram vr tayar zaleli diagram screen vr diste

if __name__ == "__main__":
    main()