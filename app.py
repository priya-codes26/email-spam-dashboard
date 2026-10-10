import streamlit as st
import pickle

st.set_page_config(
    page_title="Email Spam Dashboard",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Email Spam Dashboard")
st.write("Welcome to Email Spam Detection!")

col1, col2, col3 = st.columns(3)

col1.metric("Total Emails", 1000)
col2.metric("Spam Emails", 250)
col3.metric("Safe Emails", 750)

st.subheader("Check Your Email")

email = st.text_area("Enter your email message")
if st.button("Check Spam"):
    if email.strip():
        with open("model.pkl", "rb") as file:
            model = pickle.load(file)

        result = model.predict([email])[0]

        if result == "spam":
            st.error("This email is SPAM!")
        else:
            st.success("This email is NOT SPAM.")
    else:
        st.warning("Please enter an email message.")
