import streamlit as st
import requests
from datetime import datetime

API_URL = "http://127.0.0.1:8000"

def add_udate_tab():
    selected_date = st.date_input("Pick a date: ", datetime(2025, 1, 1), label_visibility="collapsed")
    response = requests.get(f"{API_URL}/expenses/{selected_date}")

    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error("Failed to retrieve expenses!")
        existing_expenses = []

    categories = ["Select Category", "Food", "Rent", "Shopping", "Entertainment", "Other"]

    with st.form(key="Expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Category")
        with col3:
            st.text("Notes")

        expenses = []
        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = "Select Category"
                notes = ""

            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    value=amount,
                    step=0.0,
                    key=f"amount_i{i}",
                    label_visibility="collapsed"
                )
            with col2:
                
                category = category if category in categories else "Select Category"
                default_idx = categories.index(category)
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=default_idx,
                    key=f"category_{i}",
                    label_visibility="collapsed"
                )

            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"notes_{i}",
                    label_visibility="collapsed"
                )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense["amount"] > 0]
            post_response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)

            if post_response.status_code == 200:
                st.success("Expenses successfully updated.")
            else:
                st.error("Failed to update expenses.")





