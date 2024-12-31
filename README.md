# CSV File Handling in Python

## Overview

CSV (Comma-Separated Values) files are widely used for storing tabular data. Python provides several ways to handle CSV files effectively. This guide explains how to perform CRUD (Create, Read, Update, Delete) operations on CSV files and manipulate data.

---

## Prerequisites

Before working with CSV files, ensure you have the following basic knowledge:

- Python basics (functions, loops, file handling).
- The `csv` module (built into Python).

---

## 1. Writing Data (Create)

To write data into a CSV file:

```python
import csv

# Data to write
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# Write to a CSV file
with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to data.csv")
```

---

## 2. Reading Data (Read)

To read data from a CSV file:

```python
import csv

# Read from a CSV file
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

---

## 3. Appending Data (Update)

To add data to an existing CSV file:

```python
import csv

# Data to append
new_data = [
    ["Dave", 40, "Houston"],
    ["Eve", 28, "Seattle"]
]

# Append data to the file
with open("data.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(new_data)

print("Data appended to data.csv")
```

---

## 4. Updating Specific Data

To update specific rows, read the file, modify the data, and write it back:

```python
import csv

# Read and update data
data = []
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == "Alice":  # Update Alice's age
            row[1] = 26
        data.append(row)

# Write updated data back to the file
with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data updated in data.csv")
```

---

## 5. Deleting Specific Data

To delete a row, filter out the unwanted row and write back the remaining data:

```python
import csv

# Read and filter data
data = []
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != "Bob":  # Remove Bob's row
            data.append(row)

# Write filtered data back to the file
with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Row deleted from data.csv")
```

---

## 6. Advanced Data Manipulation with Pandas

For more complex operations, use the `pandas` library:

```python
import pandas as pd

# Load data into a DataFrame
data = pd.read_csv("data.csv")
print(data)

# Update a column
data.loc[data["Name"] == "Charlie", "Age"] = 36

# Save updated data back to CSV
data.to_csv("data.csv", index=False)
print("Data updated using pandas")
```

---

## Best Practices

- Always use `newline=""` when writing to CSV files to avoid extra blank lines.
- Use `encoding="utf-8"` to handle special characters.
- Always close the file or use the `with open()` statement to handle files safely.

---

## Example Files

Save the Python scripts in `.py` files and run them to create and manipulate CSV files. Use the following sample CSV data:

**Sample `data.csv`:**

```csv
Name,Age,City
Alice,25,New York
Bob,30,Los Angeles
Charlie,35,Chicago
```
