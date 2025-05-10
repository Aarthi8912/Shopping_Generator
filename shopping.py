import streamlit as st
import cohere

# Replace this with your real Cohere API key
COHERE_API_KEY = "api_key"

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

# Streamlit UI
st.set_page_config(page_title="🛍️ Product Recommender", page_icon="🛒")
st.title("🛍️ AI Product Recommender")
st.write("Enter your product preferences and let AI suggest the best products!")

# User input
preferences = st.text_area("Enter your product preferences:",
                           placeholder="e.g. Black running shoes under Rs. 10,000, good for long-distance running")

if st.button("🔍 Recommend"):
    if not preferences.strip():
        st.warning("Please enter your product preferences.")
    else:
        with st.spinner("Generating recommendations..."):

            # Call Cohere Chat
            response = co.chat(
                model='command-r-plus',
                message=(
                    f"I am looking for product recommendations based on the following preferences: {preferences}. "
                    "Please suggest products from trusted websites like Amazon, Flipkart, or Google Shopping, and list key attributes like brand, price, and features."
                )
            )

        # Display result
        st.subheader("🛒 Recommendations:")
        st.markdown(response.text.strip())
