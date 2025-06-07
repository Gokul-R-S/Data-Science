

<h1 align="center">AtliQo Bank Credit Card Launch</h1>

This project helps AtliQo Bank, a newly launched financial institution, identify and target customers for its first credit card product. It consists of two phases:

* **Phase 1**: Identify the ideal target market
* **Phase 2**: Run an A/B test to evaluate the credit card campaign's effectiveness

---

##  **Problem Statement**

AtliQo Bank is launching its first credit card. The goals are to:

1. Identify the optimal target segment based on customer demographics and financial behavior.
2. Conduct an A/B test to determine if the credit card leads to increased customer spending.

---

##  **Project Structure**

```
├── Datasets            # All the necessary files
├── Phase_1.ipynb       # Data Cleaning, EDA, Segmentation
├── Phase_2.ipynb       # A/B Testing, Statistical Validation
├── README.md           # Project Overview
```

---

##  **Phase 1: Target Market Identification**

### **Key Activities:**

* Data cleaning and preprocessing
* Exploratory data analysis (EDA)
* Customer segmentation based on:

  * Demographics (Age, Income, Gender)
  * Behavioral data (Transaction amounts, categories)
* Visualization of insights to support strategic segmentation

### **Tools & Libraries:**

* `pandas`, `numpy` for data manipulation
* `matplotlib`, `seaborn` for data visualization

---

##  **Phase 2: A/B Testing**

### **Key Activities:**

* Business analysis of an untapped market (Age group: 18–25)
* Hypothesis testing using:

  * Power analysis
  * t-tests for comparing control and treatment groups
* Interpretation of statistical significance
* Strategic recommendations based on the results

### **Tools & Libraries:**

* `scipy`, `statsmodels` for statistical analysis
* `matplotlib`, `seaborn` for result visualization

---

## **Key Insights**

* The **18–25 age group** represents \~25% of the customer base but shows **low credit card usage** and **limited credit history**.
* This segment prefers spending in **Electronics**, **Fashion & Apparel**, and **Beauty & Personal Care**.
* Despite lower income, they demonstrate **high transaction potential** in selected categories.
* A/B testing confirmed a **significant lift in spending** when targeted with the credit card offering.

---

## **Requirements**

Install the following Python libraries before running the notebooks:

```bash
pip install pandas numpy matplotlib seaborn scipy statsmodels
```

---

## **How to Use**

1. Clone the repository.
2. Run `Phase_1.ipynb` to explore the dataset and identify the target market.
3. Run `Phase_2.ipynb` to perform A/B testing and validate the campaign strategy.

---

## **Conclusion**

The project successfully identified the 18–25 age group as a high-potential but underutilized market for credit cards. A/B testing confirmed that offering the credit card to this segment led to a **statistically significant increase in average transaction value**. These findings support a **targeted rollout** of the product to drive engagement and spending.
