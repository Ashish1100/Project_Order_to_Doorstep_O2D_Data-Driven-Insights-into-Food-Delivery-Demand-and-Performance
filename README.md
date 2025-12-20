# Order to Doorstep (O2D): Data-Driven Insights into Food Delivery Demand

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Data Science](https://img.shields.io/badge/Data_Analysis-Pandas_&_NumPy-150458?style=flat-square&logo=pandas&logoColor=white)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib_Seaborn_Plotly_&_Sweetviz-008080?style=flat-square&logo=tableau&logoColor=white)
![Status](https://img.shields.io/badge/Project_Status-Completed-success?style=flat-square)

## Project Overview
**Order to Doorstep (O2D)** is a comprehensive data analysis project focused on **FoodHub**, a food aggregator company operating in New York City. As urban lifestyles become increasingly hectic, the demand for convenient online food delivery has surged.

This project utilizes **Exploratory Data Analysis (EDA)** to examine FoodHub's order-level data. By analyzing the interplay between customers, restaurants, and delivery partners, the project aims to uncover actionable insights into demand patterns, operational bottlenecks, and customer satisfaction drivers.

---

## Business Context
FoodHub operates as a centralized marketplace connecting three key stakeholders:
1.  **Customers:** Users placing orders via a smartphone app.
2.  **Restaurants:** Establishments receiving and preparing orders.
3.  **Delivery Partners:** Logistics personnel managing the pickup and last-mile delivery.

**Revenue Model:** The company generates revenue by collecting a fixed margin on delivery orders from restaurants.

**The Challenge:**
To sustain growth and improve customer retention, FoodHub needs to leverage its data to understand:
* Which restaurants and cuisines drive the most demand?
* How do preparation and delivery latencies impact customer ratings?
* What are the distinct behaviors between weekday and weekend traffic?

---

## Project Objectives
As a Data Scientist for FoodHub, the primary goals of this analysis are:

-   **Demand Analysis:** Identify high-performing restaurants and trending cuisines.
-   **Behavioral Profiling:** Understand customer ordering habits and rating distributions.
-   **Operational Efficiency:** Evaluate the relationship between food preparation time, delivery time, and overall service quality.
-   **Strategic Optimization:** Provide data-backed recommendations to improve logistics and customer experience.

---

## Dataset Description
The analysis is based on a historical dataset of food orders processed via the FoodHub portal.

| Feature | Description |
| :--- | :--- |
| `order_id` | Unique identifier for each order. |
| `customer_id` | Unique identifier for the customer. |
| `restaurant_name` | Name of the restaurant. |
| `cuisine_type` | Type of cuisine ordered (e.g., American, Japanese). |
| `cost_of_the_order` | Total cost of the order (in dollars). |
| `day_of_the_week` | Indicator of transaction timing: **Weekday** (Mon-Fri) or **Weekend** (Sat-Sun). |
| `rating` | Customer satisfaction rating (scale 1-5). |
| `food_preparation_time` | Time (in minutes) from order confirmation to pickup. |
| `delivery_time` | Time (in minutes) from pickup to customer drop-off. |

---

## Methodology
The project follows a structured data science workflow:

1.  **Data Preprocessing & Understanding**
    * Inspection of dataset structure (shape, data types).
    * Handling missing values and data inconsistencies.
    * Statistical summary of numerical and categorical variables.

2.  **Univariate Analysis**
    * Distribution analysis of costs, ratings, and time metrics.
    * Frequency analysis for restaurants and cuisines.
    * Comparative volume analysis: Weekday vs. Weekend.

3.  **Multivariate Analysis**
    * Correlation studies: Preparation Time vs. Delivery Time.
    * Impact analysis: How wait times affect Customer Ratings.
    * Segmentation: Demand patterns by Cuisine and Restaurant.

4.  **Insight Generation**
    * Deriving business-centric conclusions from visual data.
    * Formulating strategic recommendations.

---

## Tools & Technologies

* **Programming Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn, Plotly, Sweetviz
* **Environment:** PyCharm / VS Code / Jupyter Notebook / Google Colab
* **Version Control:** Git & GitHub

---

## Key Insights
* **Demand Concentration:** A small subset of cuisines and restaurants accounts for the majority of order volume.
* **Temporal Patterns:** Weekends show a significantly higher volume of orders compared to weekdays, necessitating dynamic resource allocation.
* **Operational Impact:** Extended delivery and preparation times show a negative correlation with customer ratings, highlighting the need for logistics optimization.
* **High-Value Customers:** Orders with higher costs often come with implicit expectations for service speed and quality.

---

## Business Recommendations
1.  **Vendor Partnership Program:** Prioritize relationship management and promotional support for top-tier restaurants driving the most volume.
2.  **Dynamic Staffing:** Scale delivery partner availability during weekend peak hours to reduce delivery times.
3.  **Process Optimization:** Collaborate with restaurants showing high preparation times to streamline kitchen workflows.
4.  **Incentive Structure:** Implement performance-based incentives for delivery partners to minimize "pickup-to-drop" latency.

---

## Project Structure

```text
Order to Doorstep (O2D)/
│
├── data/
│   └── foodhub_order.csv                            # Raw order dataset
│
├── notebooks/
│   └── Project_O2D_Data_Analysis_Notebook.ipynb     # Complete data analysis notebook
│   └── Project_O2D_Data_Analysis_Notebook.html
│
├── reports/
│   └── Project_O2D_Data_Analysis_Report.pdf         # Final report / presentation of findings
│
├── src/
│   ├── data_cleaning.py                             # Data loading, cleaning, and preprocessing helpers
│   ├── data_visualization.py                        # Plotting and visualization utilities
│   └── analysis_helpers.py                          # Helper functions for metrics and business logic
│
├── main.py                                          # Script to execute the analysis workflow
├── README.md                                        # Project documentation (this file)
└── requirements.txt                                 # Dependency list
```
---
## Author

- **Name**: *Ashish Saha*
- **Role**: Data Science & Artificial Intelligence
- **Email**: [ashishsaha.software@gmail.com](mailto:ashishsaha.software@gmail.com)
- **LinkedIn**: [linkedin.com/in/ashishsaha21](https://www.linkedin.com/in/ashishsaha21)
- **GitHub**: [github.com/Ashish1100](https://github.com/Ashish1100)

---

## Contributing
Feel free to **fork**, **adapt**, and **extend** this project for further analysis.

---

## License
> This project is a personal academic initiative developed for **educational purposes and non-commercial** use only.
