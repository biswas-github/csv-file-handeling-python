import csv
data=[
    ["name","age","city"],
    ["biswas",34,"pkr"],
    ["rohan",22,"ktm"]
]
with open("data.csv",'w',newline="" ) as file:
    writer=csv.writer(file)
    writer.writerows(data)
    
