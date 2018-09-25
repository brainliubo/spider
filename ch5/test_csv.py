import csv
with open ("data.csv","w",newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["id","name", "age"])
    writer.writerow(["1","kiubo",18])
    writer.writerow(["2", "kiubo2", 28])



with open ("data.csv","r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    print(type(reader))
    for row in reader:
        print(row)