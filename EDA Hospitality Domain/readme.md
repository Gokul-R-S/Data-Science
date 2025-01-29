# AtliQ Hotels Data Analysis Project

## Overview

This project focuses on **Exploratory Data Analysis (EDA)** in the hospitality domain. The analysis is performed on hotel booking data, including various factors such as booking platforms, occupancy rates, revenue generation, and customer ratings. The goal is to uncover insights that can improve hotel operations, revenue optimization, and customer satisfaction.

## Datasets

The project utilizes the following datasets:

1. **dim\_date.csv** - Contains date-related information.
2. **dim\_hotels.csv** - Details of hotels, including hotel types and locations.
3. **dim\_rooms.csv** - Room category details for each property.
4. **fact\_aggregated\_bookings.csv** - Aggregated booking data including capacity, occupancy, and successful bookings.
5. **fact\_bookings.csv** - Individual booking transactions including revenue generated and guest details.

## Key Insights

Most hotel bookings come from the "others" category, followed by Makeyourtrip and Logtrip. The dataset covers 25 properties, with the highest-capacity property (ID: 17558) having 92 rows of data. Extreme revenue outliers beyond three standard deviations were removed to maintain data integrity. 

Delhi has the highest occupancy rate at 62.47%, while Bangalore has the lowest at 56.44%. Occupancy is generally higher on weekends. Despite Delhi leading in occupancy, Mumbai generates the highest revenue (668M), whereas Delhi generates the least (294M). This suggests Mumbai benefits from higher room rates or a larger hotel inventory.

RT2-tier hotels contribute the most revenue, with Mumbai having the highest number of RT2 reservations. Delhi also receives the highest average customer rating, while Bangalore has the lowest. Monthly revenue trends indicate a peak in May 2022, followed by a decline through December, with a notable dip in January 2022.

## Conclusion

This EDA provides valuable insights into the hospitality domain, highlighting key trends in hotel occupancy, revenue generation, and customer preferences. The findings can be used to optimize hotel pricing, improve customer experience, and enhance operational efficiency.

## Technologies Used

- **Python** (pandas, numpy, matplotlib, seaborn)
- **Jupyter Notebook** for EDA

## Future Enhancements

- **Predictive Modeling**: Building machine learning models to forecast occupancy and revenue.
- **Customer Segmentation**: Identifying key customer segments to tailor marketing strategies.
- **Pricing Optimization**: Analyzing pricing strategies to maximize revenue.

---

This project is a part of exploratory data analysis (EDA) in the hospitality domain and aims to generate meaningful insights for data-driven decision-making.

