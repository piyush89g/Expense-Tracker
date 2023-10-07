import streamlit as st
from PIL import Image
import os
import datetime
import sqlite3

from datetime import datetime

print(datetime.now())

# Set up the layout of the page
st.title("Expense Tracker")
st.write("Welcome to our Expense Tracker! Please enter your expenses below.")

# Create a form to collect user input

with st.form("expense_tracker"):
    # Add fields for date, category, amount, and description
    date = st.date_input("Date", value=datetime.now())
    category = st.selectbox("Category", ["Cab", "Food", "Flight Seat", "Flight", "Others"])
    
    flight = st.selectbox("Flight", ["AirAsia", "Vistara", "Indigo", "Akasa", "Spicejet", "StarAir", "AirIndia"], disabled=True)
    
    # Enable the flight dropdown if the category is "Flight"
    if category == "Flight":
        flight.disabled = False 
        
    amount = st.number_input("Amount", step=10)
    description = st.text_area("Description", height=150)
    
    # Add file upload field for invoice
    invoice = st.file_uploader("Invoice (PDF or image)", type=["pdf", "jpg", "png"], accept_multiple_files= True)
    
    # Submit button
    submit = st.form_submit_button("Submit")

if submit:
    # Save data to database
    db = sqlite3.connect("expenses.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO expenses VALUES (?, ?, ?, ?, ?)", (date, category, amount, description, invoice))
    db.commit()
    db.close()
    
    # Display success message
    st.success("Your expense has been added successfully!")
else:
    # Display error message if submission failed
    st.error("There was an error submitting your expense. Please try again later.")