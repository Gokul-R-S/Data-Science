import streamlit as st
from add_update import add_update_tab
from analytics_category import analytics_category_tab
from analytics_months import analytics_months_tab

st.set_page_config(page_title="Expense Tracker", page_icon="💰")
st.title("💰 Expense Tracking System")
st.markdown("*Track, analyze, and manage your expenses efficiently*")
tab1, tab2, tab3 = st.tabs(["📝 Add/Update Expenses", "📊 Category Analysis", "📅 Monthly Trends"])

with tab1:
    add_update_tab()
with tab2:
    analytics_category_tab()
with tab3:
    analytics_months_tab()

