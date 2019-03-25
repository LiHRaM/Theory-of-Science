import matplotlib.pyplot as plt
import csv
import numpy

# Load data
data = []
with open('vitdata.txt') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        data.append(row)
headers = data.pop(0)
headers, len(data)

# Assignment A
def h1():
    """The probability that a student gets question 1 right is 50%"""
    labels = "Har svaret rigtigt", "Har svaret forkert"
    plot = [
        [int(n[2]) for n in data if n[2] == '1'], 
        [int(n[2]) for n in data if n[2] == '0']
    ]
    plt.hist(plot)
    plt.show()

def h2():
    """The average total that students obtain is less than 50 points"""
    plot = [int(n[10]) for n in data if n[10] != 'Total']
    plt.boxplot(plot)
    plt.show()

def h3():
    """BLA students get better exam results than CRU students"""
    labels = "CRU", "BLA"
    plot = [
        [int(n[10]) for n in data if n[10] and n[0] == "'CRU'"],
        [int(n[10]) for n in data if n[10] and n[0] == "'BLA'"]
    ]
    plt.boxplot(plot, labels=labels)
    plt.show()

def h4():
    """Question 5 is more difficult than question 8"""
    labels = "Q5", "Q8"
    plot = [
        [int(n[6]) for n in data],
        [int(n[9]) for n in data]
    ]
    plt.boxplot(plot, labels=labels)
    plt.show()

h1()
# h2()
# h3()
# h4()