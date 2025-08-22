# COVID-19 Global EDA  

Exploratory Data Analysis of the **WHO COVID-19 global daily dataset**.  
This project covers data cleaning, feature engineering, and univariate, bivariate, and multivariate analysis with visualizations.  

---

## 📊 Project Workflow
- **Data Cleaning**  
  - Fixed missing values and corrected negative daily records using cumulative totals.  
  - Split into *active days* vs *no-case days*.  

- **Feature Engineering**  
  - 7-day rolling averages for cases & deaths.  
  - Case Fatality Ratio (CFR).  
  - Growth ratios and days since first case.  

- **Exploratory Analysis**  
  - *Univariate*: distributions, top countries, outliers.  
  - *Bivariate*: correlations, cases vs deaths, region comparisons.  
  - *Multivariate*: groupby summaries, pivot tables, correlation heatmap, country profiles.  

- **Visualization**  
  - Seaborn & Matplotlib plots.  
  - Plotly interactive charts and maps.  

- **Insights**  
  - COVID-19’s impact was unevenly distributed across countries and regions.  
  - Strong correlation between cases and deaths.  
  - Significant variation in fatality ratios (CFR) across regions.  

---

## 🚀 How to Run
1. Clone this repo.  
2. Open the Jupyter Notebook:  
   ```bash
   jupyter notebook COVID-19.ipynb
