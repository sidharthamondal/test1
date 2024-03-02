import streamlit as st
import joblib

# Load the trained model
model = joblib.load('house_price_model.joblib')

# Streamlit app title
st.title('House Price Prediction App')

# Input fields for user data
size = st.number_input('House Size (in square feet)', min_value=100.0, max_value=10000.0, value=1500.0, step=100.0)
bedrooms = st.slider('Number of Bedrooms', min_value=1, max_value=5, value=3)

# Predict button
if st.button('Predict Price'):
    # Reshape input data for the model
    input_data = [[size, bedrooms]]

    # Predict the house price
    predicted_price = model.predict(input_data)

    # Display the prediction
    st.write(f"Estimated House Price: ${predicted_price[0]:,.2f}")

# Instructions on how to use the app
st.write("""
### Instructions:
1. Adjust the house size using the number input.
2. Select the number of bedrooms using the slider.
3. Click 'Predict Price' to see the estimated price based on your inputs.
""")
