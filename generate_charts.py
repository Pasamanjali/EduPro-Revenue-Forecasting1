import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
def create_chart1():
    df = pd.read_csv("data/courses.csv")

# Create graph
    plt.figure(figsize=(8,5))

    plt.scatter(df["Marketing_Spend"],
                  df["Students_Enrolled"])

    plt.title("Marketing Spend vs Students")

    plt.xlabel("Marketing Spend")

    plt.ylabel("Students Enrolled")

    plt.grid(True)

    plt.savefig("static/images/chart1.png")

    plt.close()

    print("Chart created successfully!")