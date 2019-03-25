import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import statistics as st

import csv
data = []
with open("vitdata.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)
data.pop(0)

def h3():
    # Hypothesis: BLA results <= CRU results
    # One-sided two-sample t-test
    bla = [int(n[10]) for n in data if n[0] == "'BLA'"]
    cru = [int(n[10]) for n in data if n[0] == "'CRU'"]

    bl_avg, cr_avg = st.mean(bla), st.mean(cru)

    t = two_sample_t(bla, cru, bl_avg, cr_avg)
    cdf_val = get1DCdf(0.01)
    print(t, cdf_val, t > cdf_val)
    # Output: -0.7728593527696717 1.1920188040214295 False
    # BLA results are not <= CRU results
    # Therefore BLA > CRU (H3 is true)

def h4():
    # Hypothesis: Question 8 <= Question 5 
    # (if this is rejected, then Q5 < Q8, which is what we _really_ want to know).
    # One-sided two-sample t-test
    
    q5 = [int(n[6]) for n in data]
    q8 = [int(n[9]) for n in data]

    q5_avg, q8_avg = st.mean(q5), st.mean(q8)

    t = two_sample_t(q5, q8, q5_avg, q8_avg)
    cdf_val = get1DCdf(0.01)
    print(t, cdf_val, t > cdf_val)
    # Output: 10.665416087997425 1.1920188040214295 True
    # We can therefore reject the hypothesis and accept H4

def get1DCdf(alpha):
    return stats.norm.cdf(1-alpha)**-1

def variance(list, avg):
    return st.mean([(n - avg)**2 for n in list])

def two_sample_t(l1, l2, l1_avg, l2_avg):
    k, l = float(len(l1)), float(len(l2))
    avg = (l1_avg - l2_avg)
    sq1 = math.sqrt(sum([(n - l1_avg)**2 for n in l1]) + sum([(n - l2_avg)**2 for n in l2]))
    sq2 = math.sqrt((k + l - 2) / (1 / k + 1 / l))
    return (avg / sq1) * sq2

h3()
h4()
