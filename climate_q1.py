import matplotlib.pyplot as plt
import sqlite3

# Connect to the SQLite database (replace 'your_database.db' with your database file)
con = sqlite3.connect('climate.db')
db = con.cursor()

# Execute a query to fetch data from the database (adjust the query as per your database schema)
db.execute("select Year, CO2, Temperature from ClimateData")

# Fetch all the rows from the query result
data = db.fetchall()

# Separate the data into lists
years = [row[0] for row in data]
co2 = [row[1] for row in data]
temp = [row[2] for row in data]

# Close the database connection
con.close()

# Plot the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.savefig("co2_temp_1.png")
plt.show()