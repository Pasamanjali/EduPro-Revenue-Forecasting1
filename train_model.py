import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/courses.csv")

# Check the dataset
print("Dataset Shape:", df.shape)
print(df.head())
print(df.info())
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nCorrelation:")
print(df.corr(numeric_only=True))
# Encode Category
label_encoder = LabelEncoder()
df["Category"] = label_encoder.fit_transform(df["Category"])

# Features (Input)
X = df[["Category", "Price", "Rating", "Duration", "Marketing_Spend"]]

# Target (Output)
y = df["Students_Enrolled"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate the model
print("\nModel Evaluation")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Save the model
joblib.dump(model, "models/revenue_model.pkl")
print("\nModel saved successfully!")