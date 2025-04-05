import streamlit as st
import pandas as pd
from utils import fetch_data, API_URL

def analytics_months_tab():
    data = fetch_data(
        f'{API_URL}/months',
        data_type="monthly data",
        default_empty={}
    )

    if data is None:
        return

    if not data:
        st.error("❌ **No data available.**")
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
        df=df.set_index('Months')['Total']
        st.table(df)

    except (KeyError, TypeError) as e:
        st.error("❌ **Error processing analytics data:** Invalid format or missing keys.")
        st.markdown(f"```{str(e)}```", unsafe_allow_html=True)

    except Exception as e:
        st.error("❌ **Unexpected error while rendering monthly analytics.**")
        st.markdown(f"```{str(e)}```", unsafe_allow_html=True)

if __name__ == "__main__":
    analytics_months_tab()