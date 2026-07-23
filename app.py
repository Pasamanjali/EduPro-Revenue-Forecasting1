from flask import Flask, render_template, request
from generate_charts import create_chart1
import joblib
import pandas as pd
import sqlite3

app = Flask(__name__)

# Load the trained model
model = joblib.load("models/revenue_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():

    df = pd.read_csv("data/courses.csv")

    total_courses = len(df)

    average_rating = round(df["Rating"].mean(),2)

    highest_price = df["Price"].max()

    total_students = df["Students_Enrolled"].sum()
    
    average_price = round(df["Pprice"].mean(), 2)

    return render_template(
        "dashboard.html",
        total_courses=total_courses,
        average_rating=average_rating,
        highest_price=highest_price,
        total_students=total_students,
        average_price=average_price
    )

@app.route("/history")
def history():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM predictions ORDER BY id DESC")

    records = cursor.fetchall()

    conn.close()

    return render_template("history.html", records=records)

@app.route("/predict", methods=["POST"])
def predict():

    category = int(request.form["category"])
    price = float(request.form["price"])
    rating = float(request.form["rating"])
    duration = int(request.form["duration"])
    marketing = float(request.form["marketing"])
    
    if price <= 0:
        return render_template("index.html",error="Price must be greater than 0.")
    
    if rating < 1 or rating > 5:
        return "Rating must be between 1 and 5."
    
    if duration <= 0:
        return "Duration must be greater than 0."
    
    if marketing <= 0:
        return "Marketing Spend must be greater than 0."

    input_data = pd.DataFrame({
         "Category": [category],
         "Price": [price],
         "Rating": [rating],
         "Duration": [duration],
         "Marketing_Spend": [marketing]
    })

    prediction = model.predict(input_data)
    predicted_students = prediction[0]
    expected_revenue = predicted_students * price
    predicted_students = round(prediction[0])
    revenue = predicted_students * price
    
    
    create_chart1()
    
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions
    (category, price, rating, duration, marketing, students, revenue)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        str(category),
        price,
        rating,
        duration,
        marketing,
        predicted_students,
        revenue
    ))

    conn.commit()
    conn.close()
    
    if predicted_students >= 600:
       demand = "High Demand 🔥"

    elif predicted_students >= 400:
         demand = "Medium Demand ⭐"

    else:
        demand = "Low Demand 📉"


    return render_template(
       "result.html",
       predicted_students=round(predicted_students, 2),
       prediction=predicted_students,
       revenue=round(expected_revenue, 2),
       demand=demand,
       chart="images/chart1.png"
)
    



if __name__ == "__main__":
    app.run(debug=True)