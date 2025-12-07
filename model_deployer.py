import streamlit as st
import pickle
model = pickle.load(open(r"D:\ML Models 5th unit\model.pkl", "rb"))
vectorizer = pickle.load(open(r"D:\ML Models 5th unit\vectorizer.pkl", "rb"))
st.title("SMS Spam Detection App")
st.write("Type a message below to check if it's spam or ham.")
user_input = st.text_area("Enter SMS message:")
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        # Transform input
        transformed = vectorizer.transform([user_input])
        prediction = model.predict(transformed)[0]

        if prediction == 1:
            st.error("🚫 This message is **SPAM**.")
        else:
            st.success("✅ This message is **HAM**.")
