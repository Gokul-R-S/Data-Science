import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    response=requests.get(f'{API_URL}/months')
    response=response.json()
    data={
        'month_num': [row['month_num'] for row in response],
        'Months':[ row['months'] for row in response ],
        'Total': [row['total'] for row in response]
    }

    df = pd.DataFrame(data)

    st.title('Expense Breakdown By Months')

    st.bar_chart(data=df.set_index('Months')['Total'], width=0, height=0, use_container_width=True)
    df['Total'] = df['Total'].map('{:.2f}'.format)

    df.set_index('month_num',inplace=True)

    st.table(df)