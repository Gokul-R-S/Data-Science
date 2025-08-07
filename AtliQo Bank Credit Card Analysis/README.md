<h1 align="center">AtliQo Bank Credit Card Analysis</h1>

This project analyzes customer data to identify the ideal target market for **AtliQo Bank's** first credit card and evaluates its effectiveness through an **A/B test**. The analysis focuses on **data cleaning, imputation, outlier treatment, statistical testing**, and **business insights**.

## Project Overview
AtliQo Bank aims to target customers most likely to have higher transaction amounts.  
The project involves:

1. **Data Preprocessing**
   - Imputation of missing values for income, age, credit limit, and platform.
   - Outlier treatment for transaction amounts using product-category means.
   - Capping outstanding debt to the maximum credit limit.
   - Duplicate removal for credit score data.

2. **Exploratory Insights**
   - Amazon dominates transaction counts, but average transaction amounts remain similar across platforms.

3. **A/B Testing**
   - **Population:** Customers aged 18–25.
   - **Design:** Test group (credit card campaign) vs control group.
   - **Statistical Method:** One-tailed Welch’s *t*-test.
   - **Result:** Test group’s average transaction amount was significantly higher than the control group’s.

## Key Results
- The test group outperformed the control group in average transaction amount.
- Statistical testing confirmed the difference was significant.
- The confidence interval for the test group’s mean was entirely above the control group’s mean.

## Tools & Libraries
- Python (pandas, numpy, scipy, matplotlib, seaborn)
- Statistical methods (Shapiro-Wilk, Levene’s test, Welch’s t-test)
- Data visualization

## Conclusion
The statistical evidence supports launching the new credit card to a broader audience, targeting the identified customer segment.