# Order to Doorstep (O2D): Data-Driven Insights into Food Delivery Demand

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Data Science](https://img.shields.io/badge/Data_Analysis-Pandas_&_NumPy-150458?style=flat-square&logo=pandas&logoColor=white)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib_Seaborn_Plotly_&_Sweetviz-008080?style=flat-square&logo=tableau&logoColor=white)
![Status](https://img.shields.io/badge/Project_Status-Completed-success?style=flat-square)

> "Optimizing the journey from kitchen to customer through data-driven intelligence."

---

## Project Overview
**Order to Doorstep (O2D)** is a comprehensive data analysis project focused on **FoodHub**, a food aggregator company. As urban lifestyles become increasingly hectic, the demand for convenient online food delivery has surged.

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

## Architecture

![Architecture ](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/architecture.png)


![Strategy](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/STRATEGY.png)

---

## Dataset Description

The analysis is based on a snapshot of FoodHub's order history.

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

## Key Insights & Findings

After rigorous Exploratory Data Analysis (EDA), the following patterns emerged:

### 1. The Weekend Surge
*   **Insight:** Demand is not uniform. The data reveals a massive disparity between weekend and weekday activity.
*   **Data:** **1,351 orders** were placed on weekends compared to just **547** on weekdays.
*   **Implication:** Operations must be scaled elastically; a static fleet size will be inefficient on weekdays and overwhelmed on weekends.

### 2. The "Shake Shack" Effect
*   **Insight:** A small number of restaurants dominate the order volume (Pareto Principle).
*   **Data:** **Shake Shack** is the undisputed leader with **219 orders**, followed by *The Meatball Shop* (132) and *Blue Ribbon Sushi* (119).
*   **Implication:** Strategic partnerships with these "Anchor Tenants" are critical for revenue stability.

### 3. The Rating Void
*   **Insight:** A significant portion of the customer base is silent.
*   **Data:** **736 orders (approx. 39%)** have no rating given. Among those who did rate, the average is high, with **588** customers giving a perfect 5-star rating.
*   **Implication:** The "silent majority" represents a blind spot in quality control.

### 4. Operational Latency
*   **Insight:** Total delivery time (Prep + Travel) varies significantly.
*   **Data:** 
    *   **Preparation Time:** Ranges from 20 to 35 minutes.
    *   **Delivery Time:** Ranges from 15 to 33 minutes.
*   **Implication:** Customers ordering from "Slow Prep" restaurants during "High Traffic" weekends face the longest wait times, risking churn.

---

## Visualizations

*Note: The following plots were generated during the analysis to visualize distributions and correlations.*

### Cuisine Popularity
![Cuisine_revenue](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/Cuisines_revenue.png)

![cuisines](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/cuisines.png)

![cuisines_1](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/cuisines_1.png)

### Delivery Time Distribution
![Delivery Time](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/Delivery_time.png)

![Delivery Time](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/Percentage_of_Orders_Taking_60_mins.png)

### Customer Ratings

![Rating](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/Rating.png)

![Customer_Ratings](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/Customer_Ratings.png)

### Restaurants

![Top_10_Revenue_Generating_Restaurants](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/Top_10_Revenue_Generating_Restaurants.png)

![High_Performing_Restaurants](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/High_Performing_Restaurants.png)

### Top Customers

![Top_5 Most_Frequent_Customers](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/Top_5%20Most_Frequent_Customers.png)


### Correlation Heatmap

![Correlation_Heatmap](https://github.com/Ashish1100/Project_Order_to_Doorstep_O2D_Data-Driven-Insights-into-Food-Delivery-Demand-and-Performance/blob/main/images/correlation_matrix.png)

---

## Business Recommendations

Based on the data, I propose the following strategic actions:

1.  **Dynamic Fleet Allocation:**
    *   Implement a **Weekend Surge Fleet** model. Since demand triples on weekends, hiring part-time drivers specifically for Fri-Sun shifts will reduce delivery times without inflating weekday overhead.

2.  **"Rate to Earn" Loyalty Program:**
    *   With nearly **40% of ratings missing**, FoodHub loses critical feedback. Introduce a gamified system where customers earn "FoodHub Points" for leaving a rating, increasing data granularity.

3.  **Top Vendor Optimization:**
    *   Work directly with **Shake Shack** and **The Meatball Shop** to create dedicated "FoodHub Express Lanes" in their kitchens. Reducing their prep time by even 5 minutes would significantly improve average system-wide speed due to their high volume.

4.  **Promotional Push for Weekdays:**
    *   Launch **"Weekday Warrior"** discounts (e.g., free delivery on Tuesdays) to smooth the demand curve and utilize the delivery fleet more efficiently during low-traffic periods.

---

## Tools & Technologies

*   **Language:** Python 3.x
*   **Environment:** Jupyter Notebook / Google Colab
*   **Libraries:**
    *   `Pandas`: Data manipulation and aggregation.
    *   `NumPy`: Numerical computations.
    *   `Matplotlib` & `Seaborn`: Advanced data visualization.
    *   `Scipy`: Statistical analysis.

---

## Repository Structure

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
│   └── Project_O2D_Data_Analysis_Report.pptx
│
├── src/
│   ├── data_cleaning.py                             # Data loading, cleaning, and preprocessing helpers
│   ├── data_visualization.py                        # Plotting and visualization utilities
│   └── analysis_helpers.py                          # Helper functions for metrics and business logic
│
├── images/
│   └── # all images of results used in readme.md
│
├── main.py                                          # Script to execute the analysis workflow
├── README.md                                        # Project documentation (this file)
├── license.md                                       # License and legal 
└── requirements.txt                                 # Dependency list
```

---
## **Author**

<div align="center">

### **Ashish Saha**
**AI Engineering** | **ML Research** | **Data Science**

*Specializing in building intelligent ML systems and transforming data into actionable insights.*

<a href="https://github.com/Ashish1100" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
</a>
<a href="https://www.linkedin.com/in/ashishsaha21/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
<a href="mailto:ashishsaha.software@gmail.com">
  <img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email">
</a>

</div>

---

## Contributing
Feel free to **fork**, **adapt**, and **extend** this project for further analysis.

---

## License
> This project is a personal academic initiative developed for **educational purposes and non-commercial** use only.

<div align="center">

---

### **Star ⭐ this repo if you found this project helpful!**

---

<p><i>"Data is the new oil, but it's useless until refined."</i></p>

*Made with ❤️ by Ashish Saha*

</div>

