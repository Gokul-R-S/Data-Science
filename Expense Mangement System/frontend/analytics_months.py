import streamlit as st
import pandas as pd
from utils import fetch_data, API_URL
from backend.logging_setup import setup_frontend_logger

monthly_analytics_logger = setup_frontend_logger('monthly_analytics')

def analytics_months_tab():
    monthly_analytics_logger.info("Fetching monthly analytics data from the server.")

    data = fetch_data(
        f'{API_URL}/months',
        data_type="monthly data"
    )

    if data is None:
        return

    if not data:
        st.error("❌ **No data available.**")
        monthly_analytics_logger.info("No monthly analytics data available from the server.")
        return

    try:
        data_df = {
            'month_num': [row['month_num'] for row in data],
            'Months': [row['months'] for row in data],
            'Total': [row['total'] for row in data]
        }
        df = pd.DataFrame(data_df)

        df = df.sort_values('month_num')

        st.markdown("### **Expense Breakdown By Months**", unsafe_allow_html=True)

        st.bar_chart(data=df.set_index('Months')['Total'], use_container_width=True)

        df['Total'] = df['Total'].map('{:.2f}'.format)
        df = df.set_index('Months')['Total']
        st.table(df)

        monthly_analytics_logger.info("Monthly analytics successfully rendered on the dashboard.")

    except Exception as e:
        st.error("❌ **Unexpected error while rendering monthly analytics.**")
        monthly_analytics_logger.error(
            f"Unexpected error while rendering monthly analytics:\n"
            f"Data fetched: {data}\n"
            f"Exception: {str(e)}"
        )

if __name__ == "__main__":
    analytics_months_tab()