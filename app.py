import streamlit as st
import requests
from add_update_ui import add_udate_tab
from analytics_ui import analytics_category_tab
from analytics_months import analytics_months_tab  # NEW IMPORT

# Background color (dark theme)
st.markdown("""
    <style>
        .stApp {
            background-color:  	#1f1f1f;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Expense Tracking System")

# Now we have three tabs
tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Monthly Analytics"])

with tab1:
    add_udate_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()  # NEW FUNCTION CALL



