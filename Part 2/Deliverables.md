---
author: Hilmar Gústafsson
title: Theory of Science - Deliverables for Part II
---

# Exercise 1

## A
> For each of the four hypotheses,
>
> Determine whether it is a one sample performance hypothesis, or a two-sample comparative hypothesis
>
> Perform a preliminary investigation of the plausibility of the hypothesis using descriptive analysis tools (boxplots, histograms, biplots,...)

### H1
> The probability that a student gets question 1 right is 50%

1. One-sample performance analysis.
2. A histogram shows the columns are roughly of the same size, with slightly fewer students answering incorrectly.

### H2
> The average total that students obtain is less than 50 points.

1. One-sample performance analysis.
2. A box-plot gives the impression that a larger part of the percentage is above 50 points, with the median being slightly above, with the third and fourth quarters being significantly above.

### H3
> BLA students get better exam results than CRU students

1. Two-sample comparative analysis.
2. A box-plot shows that the CRU students' results vary more, with both a higher max and a lower min. Their median is slightly above, which of course does not say much about the mean.

### H4
> Question 5 is more difficult than question 8

1. Two-sample comparative analysis.

# Exercise 2
> C. For hypotheses H3 and H4 from Exercise 1:
>
> - Identify a statistical test that is suitable to test the hypothesis
> - Apply the test to the vitdata and determine whether the hypothesis is rejected at a significance level of 0.01.

## H3
- Two sided t-test is used to compare the values.
```python
# We use a two-sided t-test to test our hypothesis, H3: BLA students get better results than CRU students
bla = [int(n[10]) for n in data if n[0] == "'BLA'"]
cru = [int(n[10]) for n in data if n[0] == "'CRU'"]

import statistics as st
bl_avg, cr_avg = st.mean(bla), st.mean(cru)
bl_var, cr_var = st.mean([(bl_avg - n)**2 for n in bla]), st.mean([(cr_avg - n)**2 for n in cru])

t = ((bl_avg - cr_avg) / math.sqrt(sum([(n - bl_avg)**2 for n in bla]) + sum([(n - cr_avg)**2 for n in cru]))) * math.sqrt(len(bla) + len(cru) - 2) / 1/len(bla) + 1/len(cru)
cdf_val = stats.norm.cdf(1 - 0.01)**-1
t, cdf_val, t > cdf_val
# (0.006269614688396898, 1.1920188040214295, False)
```
## H4


> D. Define yourself 4 new hypotheses about the students and exam questions in vitdata, such that you have one hypothesis each with the following characteristics:
>
> - the hypothesis is one sample, and can be tested with the Binomial test
> - the hypothesis is one sample, and can be tested with the one sample t-test
> - the hypothesis is two sample, and can be tested with the two sample t-test
> - the hypothesis is two sample, and can be tested with the Wilcoxon test
> 
> For each hypothesis, perform a preliminary analysis using descriptive statistics, and based on this analysis, decide whether you think the hypothesis should be 
> 1. not rejected, 
> 2. rejected, or 
> 3. very clearly rejected (with a p-value < 0.00001)

> Apply a suitable statistical test to your hypotheses, and check whether the result of the test corresponds to your expectation.

# Exercise 3
> What is the purpose and functionality of your system (brief description)? What would be the performance measure with which you can measure the quality of your system?

The purpose of our system is node classification in a graph.

In terms of computation speed, we could measure the time it takes to train the model, or classify with it. We could also look at the accuracy of classification.

> Would there be an alternative, existing solution to which you could compare your solution?

Yes, we actually base our algorithm on a paper by Kipf and Welling, who have open-sourced their code. We can use this code as comparison.

> How do you set up an experiment to collect empirical data for the comparison?

