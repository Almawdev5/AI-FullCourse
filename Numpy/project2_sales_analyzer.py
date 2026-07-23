import numpy as np


print("========== SALES DATA ANALYZER ==========\n")


# Products
products = np.array([
    "Laptop",
    "Phone",
    "Tablet",
    "Headphones"
])


# Monthly sales data
# Rows = Products
# Columns = Months

sales = np.array([
    [120, 150, 170, 200],
    [300, 280, 350, 400],
    [100, 130, 120, 160],
    [250, 270, 300, 330]
])


months = np.array([
    "January",
    "February",
    "March",
    "April"
])


print("Products:")
print(products)

print("\nSales Data:")
print(sales)



# -------------------------------
# Total Sales Per Product
# -------------------------------

total_sales = np.sum(sales, axis=1)

print("\n----- Total Sales Per Product -----")

for i in range(len(products)):
    print(products[i], ":", total_sales[i])



# -------------------------------
# Average Monthly Sales
# -------------------------------

average_sales = np.mean(sales, axis=1)

print("\n----- Average Sales -----")

for i in range(len(products)):
    print(products[i], ":", average_sales[i])



# -------------------------------
# Best Selling Product
# -------------------------------

best_index = np.argmax(total_sales)

print("\n----- Best Product -----")

print(
    products[best_index],
    "with total sales:",
    total_sales[best_index]
)



# -------------------------------
# Highest Sales Month
# -------------------------------

monthly_total = np.sum(sales, axis=0)

best_month = np.argmax(monthly_total)

print("\n----- Best Month -----")

print(
    months[best_month],
    "with sales:",
    monthly_total[best_month]
)



# -------------------------------
# Filtering High Sales
# -------------------------------

print("\n----- High Sales Values -----")

high_sales = sales[sales > 300]

print(high_sales)



# -------------------------------
# Apply Discount
# -------------------------------

discount = np.array([
    10,
    20,
    15,
    5
])


new_sales = sales - discount[:, np.newaxis]


print("\n----- Sales After Discount -----")

print(new_sales)



# -------------------------------
# Correlation
# -------------------------------

print("\n----- Product Correlation -----")

correlation = np.corrcoef(sales)

print(correlation)



# -------------------------------
# Statistics
# -------------------------------

print("\n----- Statistics -----")

print("Maximum Sale:", np.max(sales))

print("Minimum Sale:", np.min(sales))

print("Overall Average:", np.mean(sales))

print("Standard Deviation:", np.std(sales))


print("\n========== END ==========")