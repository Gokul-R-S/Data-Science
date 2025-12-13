
# Sales and Financial Analytics for AtliQ Hardware

## Overview
This project demonstrates a complete sales and financial analytics workflow for AtliQ Hardware, transforming raw data into interactive Excel reports using Power Query and Power Pivot. It builds a star-schema data model to analyze sales performance, targets, P&L metrics, and key business insights across customers, markets, products, and divisions from 2019–2021.

## Key Outputs
### Sales Analytics (`Sales Analytics.xlsx`)
- **Customer Performance Report**: Net sales by customer (2019–2021) with YoY growth.
- **Market Performance vs Target**: Country-level sales vs. 2021 targets, including variance %.
- **Top 10 Products 2021**: Products ranked by 2020–2021 sales growth %.
- **Division Report**: Sales by division (N&S, P&A, PC) with growth.
- **Quantity Sold**: Top/bottom 5 products by total units.
- **New Products**: 2021 sales for newly introduced products.
- **Top 5 Countries**: Highest 2021 sales by country.

### Financial Analytics (`Finance Analytics.xlsx`)
- **P&L Year**: Annual Net Sales, COGS, Gross Margin, and GM% (2019–2021).
- **P&L Months**: Monthly/quarterly P&L breakdown by fiscal year.
- **P&L Markets**: P&L metrics by market (country).
- **GM% by Subzone**: Quarterly/annual GM% by region (ANZ, India, NA, NE, ROA, SE).

## Process
1. **ETL**: Loaded raw data (e.g., `fact_sales_monthly`) into Power Query for cleaning, standardization, and fiscal date calculations (e.g., `EDATE` for FY months, `ROUNDUP` for quarters).
2. **Modeling**: Star schema in Power Pivot with relationships to dimensions (date, customers, products, markets). Added measures for YoY growth, variances.
3. **Visualization**: PivotTables for interactive filtering and slicing.

## Tools
- Microsoft Excel
- Power Query (ETL & transformations)
- Power Pivot (data modeling & DAX measures)

