import matplotlib.pyplot as plt
import seaborn as sns

# Exercise 1: Line Plot for Population Over Time
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
city_a = [500000, 550000, 600000, 650000, 700000, 750000, 800000]
city_b = [800000, 850000, 900000, 950000, 1000000, 1050000, 1100000]
city_c = [1000000, 1050000, 1100000, 1150000, 1200000, 1250000, 1300000]
city_d = [1200000, 1250000, 1300000, 1350000, 1400000, 1450000, 1500000]

plt.figure(figsize=(8,5))
plt.plot(years, city_a, marker='o', label="City A")
plt.plot(years, city_b, marker='s', label="City B")
plt.plot(years, city_c, marker='^', label="City C")
plt.plot(years, city_d, marker='d', label="City D")
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population Growth Over Time")
plt.legend()
plt.grid(True)
plt.show()
# Exercise 2: Scatter Plot for Study Hours vs Test Scores
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [93, 57, 61, 54, 51, 53, 87, 81, 83, 85]

plt.figure(figsize=(8,5))
sns.scatterplot(x=study_hours, y=test_scores)
plt.xlabel("Hours Studied")
plt.ylabel("Test Scores")
plt.title("Study Hours vs Test Scores")
plt.show()
# Exercise 3: Bar Chart for Monthly Sales
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [11860, 10480, 4997, 5523, 13965, 6011, 13158, 9533, 5158, 9058, 11346, 6675]

plt.figure(figsize=(10,5))
plt.bar(months, sales, color='skyblue')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Data")
plt.xticks(rotation=45)
plt.show()