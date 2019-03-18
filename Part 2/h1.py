import matplotlib.pyplot as plt
import csv
x = []
with open('vitdata.txt') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=',')
    for row in reader:
        x.append(row["Q1"])

plt.plot(x, label="Question 1 answers")
plt.show()