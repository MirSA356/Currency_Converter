import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="💱 Currency Converter", page_icon="💱", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        font-size: 18px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stMarkdown h2 {
        color: #4CAF50;
    }
    .result {
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and description
st.title("💱 Currency Converter")
st.write("Convert currency using real-time exchange rates!")

# Function to get exchange rates
def get_exchange_rate(base_currency, target_currency):
    API_KEY = "177baaa251433248cee8cbf9"  # Replace with your API key from https://exchangerate-api.io/
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data["conversion_rates"][target_currency]
    else:
        st.error("Failed to fetch exchange rates. Please try again later.")
        return None

# Currency input
amount = st.number_input("Enter amount:", min_value=0.01, format="%.2f")

# Currency selection (including PKR)
currencies = ["USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "PKR"]
from_currency = st.selectbox("From", currencies)
to_currency = st.selectbox("To", currencies)

# Convert currency
if st.button("Convert"):
    if amount is not None:
        exchange_rate = get_exchange_rate(from_currency, to_currency)
        if exchange_rate is not None:
            converted_amount = amount * exchange_rate
            st.markdown(f"<p class='result'>Converted amount: {converted_amount:.2f} {to_currency}</p>", unsafe_allow_html=True)
    else:
        st.error("Please enter an amount to convert.")

# Footer
st.markdown("---")
st.write("Created with ❤️ by **Naseem Ahmed Detho**")
