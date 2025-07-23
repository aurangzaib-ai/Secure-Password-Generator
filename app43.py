import streamlit as st
import random
import string

# App Title
st.title("Secure Password Generator")

# Display an image for password generation
st.image("https://www.example.com/new-image.jpg", use_column_width=True)

# Function to convert letters to numbers
def convert_to_numbers(text):
    result = "".join(str(ord(char.upper()) - 64) for char in text if char.isalpha())
    return result

# User input
keyword = st.text_input("Enter your name or a word:")

# Slider to select password length
password_length = st.slider("Select password length", 8, 24, 12)

# Button to generate password
if st.button("Generate Password"):
    if keyword:
        base_password = convert_to_numbers(keyword)
        
        # Extend password to the desired length
        while len(base_password) < password_length:
            base_password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        
        # Trim the password to the exact length
        final_password = base_password[:password_length]
        
        # Display the generated password
        st.success(f"Your secure password: {final_password}")
    else:
        st.warning("Please enter a name or word!")
