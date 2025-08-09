<h1 align="center">AtliQo Bank Credit Card Analysis</h1>

This project analyzes customer data to identify the ideal target market for **AtliQo Bank's** first credit card and evaluates its effectiveness through an **A/B test**. The analysis focuses on **data cleaning, imputation, outlier treatment, statistical testing**, and **business insights**.

## Project Overview
AtliQo Bank aims to target customers most likely to have higher transaction amounts. The work is divided into two phases:

- **Phase 1 – Target Market Identification:** Cleaning and preparing customer, credit score, and transaction data to define the ideal customer segment.
- **Phase 2 – A/B Testing:** Running a statistical experiment to measure the credit card’s impact.

### Phase 1: Data Preprocessing & Insights
- Imputation of missing values for income, credit limit, and platform.
- Values deemed invalid for Age (<18 or >80) were replaced with mean per occupation.
- Outlier treatment for transaction amounts using product-category means.
- Capping outstanding debt to the maximum credit limit.
- Duplicate removal for credit score data.
- Amazon dominates transaction counts, but average transaction amounts are similar across platforms.

### Phase 2: A/B Testing
- **Population:** Customers aged 18–25.
- **Design:** Test group (credit card campaign) vs control group.
- **Statistical Method:** One-tailed Welch’s *t*-test.
- **Result:** The test group’s average transaction amount was significantly higher than the control group’s, with statistical evidence confirming the difference.

## Key Results
- The test group outperformed the control group in average transaction amount.
- Statistical testing confirmed the difference was significant.
- The confidence interval for the test group’s mean was entirely above the control group’s mean, reinforcing the campaign’s effectiveness.

## Tools & Libraries
- Python (pandas, numpy, scipy, matplotlib, seaborn)
- Statistical methods (Shapiro-Wilk, Levene’s test, Welch’s t-test)
- Data visualization

## Conclusion
The analysis demonstrates a strong case for launching the new credit card to a broader audience, focusing on the identified target market.
