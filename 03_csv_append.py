import csv
data=[
    ["shyam",13,"bagar"],
    ["none",15,"simpani"]
]
with open("data.csv",'a',newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)

# display data.csv to check if the append data is correct or not
with open("data.csv",'r') as file:
    reader=csv.reader(file)
    for rows in reader:
        checker=",".join(rows)
        print(f"{(checker)}")