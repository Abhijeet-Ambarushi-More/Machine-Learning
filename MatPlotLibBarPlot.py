import matplotlib.pyplot as plt

def main():
   language = ["C", "C++", "Java", "Python"]
   students = [30,40,35,55]

   plt.bar(
       language,                    # Values of X axis
       students,                    # Values of Y axis
       width = 0.6,                 # Width of bar
       edgecolor = "black",         # Border color of bars
       linewidth = 1,               # Width of bar order
       alpha = 0.8,                 # transperence 0.0 to 1.0
       label = "Students"           # Legend text
    )

   plt.title("Marvellous Bar Plot")
   plt.xlabel("Languages")
   plt.ylabel("Number of Students")
   plt.legend()
   plt.show()

if __name__ == "__main__":
    main()