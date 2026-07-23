import pandas as pd
import random

courses = [
    "Python Programming",
    "Java Programming",
    "SQL Basics",
    "Data Science",
    "Machine Learning",
    "Web development",
    "Cloud Computing",
    "Cyber Security",
    "Digital Marketing",
    "Excel for Beginners"
]

categories = [
    "Programming",
    "Programming",
    "Database",
    "AI",
    "AI",
    "Web",
    "Cloud",
    "Security",
    "Marketing",
    "Business"
]

data = []

for i in range(1000):
    
    index = random.randint(0,9)
    
    course = courses[index]
    category = categories[index]
    
    price = random.randint(1500,6000)
    
    rating = round(random.uniform(4.0,5.0),1)
    duration = random.randint(20,70)
    marketing_spend  = random.randint(5000,20000)
    
    students = random.randint(200,800)
    
    revenue = price * students
    
    data.append([
        course,
        category,
        price,
        rating,
        duration,
        marketing_spend,
        students,
        revenue
    ])
    
    df = pd.DataFrame(data, columns=[
        "Course",
        "Category",
        "Price",
        "Rating",
        "Duration",
        "Marketing_Spend",
        "Students_Enrolled",
        "Revenue"
    ])
    
    df.to_csv("data/course.csv",index=False)
    
    print("Dataset created successfully!")