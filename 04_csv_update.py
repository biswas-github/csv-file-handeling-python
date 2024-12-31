import csv
check_name="biswas"
change_age=0;
data=[]
# reading a file and updating the cchanges in the dictonary
with open("data.csv",'r') as file:
    reader=csv.reader(file)
    for info in reader:
        if info[0]=="biswas":
            info[1]=0
        data.append(info)
# updating the file now for making the changes in file from the dictonar...y
with open("data.csv",'w' , newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)