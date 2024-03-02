import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Create a synthetic dataset
np.random.seed(42)  # for reproducibility
sizes = np.random.normal(1500, 500, 1000)  # House sizes around 1500 sqft with some variation
bedrooms = np.random.randint(1, 5, 1000)  # Number of bedrooms between 1 and 4
prices = 100 + 0.5 * sizes + 20 * bedrooms + np.random.normal(0, 50, 1000)  # Base price + size and bedroom factors

# Create a DataFrame
data = pd.DataFrame({
    'Size': sizes,
    'Bedrooms': bedrooms,
    'Price': prices
})

# Split the data into input features (X) and target variable (y)
X = data[['Size', 'Bedrooms']]
y = data['Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# Save the trained model
joblib.dump(model, 'house_price_model.joblib')
print("Model saved successfully!")
