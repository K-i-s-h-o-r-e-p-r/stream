import streamlit as st

# Get user input as a string
t = st.text_input("Enter the age")

# Convert input to an integer if possible
if t:
    try:
        t = int(t)  # Convert to integer
        if t <18:
            st.error("FBI open up!!!")
            st.camera_input("open the damn door")
        elif t >= 18:
            st.success("good to go")
       
        print(t)
    except ValueError:
        st.error("Please enter a valid age")
    
