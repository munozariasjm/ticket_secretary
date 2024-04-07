# Ticket Secretary: Optimal Ticket Purchasing via the Secretary Problem

Ticket Secretary leverages a classic statistical theory to provide a smart, data-driven approach to purchasing tickets, aiming to save money and reduce the hassle in timing the purchase.

We coded it in a couple of hours, one of our for jokes  ;)

Ticket Secretary is a library that applies the secretary problem's statistical solution to optimize ticket purchasing for events like flights or concerts. It identifies the best time to buy tickets based on price trends and mathematical strategies.

## Secretary Problem in Depth
The secretary problem illustrates a scenario where one must choose the best option (e.g., secretary, ticket price) after seeing only a portion of the available choices. Mathematically, after reviewing \(e^{-1} \approx 37\%\) of the options, the next option better than all seen before is chosen. This strategy statistically provides the best chance of selecting the optimum choice.

### Problem Statement

```
Suppose you need to hire a secretary from a pool of \(n\) applicants. You can interview the applicants sequentially, but you must decide immediately after each interview whether to hire the candidate or move on. If you reject a candidate, you cannot return to them later. Your goal is to maximize the probability of hiring the best candidate.
```

### Solution
The formal solution to the secretary problem involves the following steps:

1. **Sampling Phase:** Interview and reject the first \( \left\lfloor \frac{n}{e} \right\rfloor \) applicants to establish a benchmark. \( e \) is the base of natural logarithms (approximately 2.71828). This phase is purely for gathering information and no selections are made here.

2. **Selection Phase:** Continue interviewing. Hire the first candidate who is better than all the candidates in the sampling phase.

By using this strategy, the probability of selecting the best candidate converges to approximately \( 1/e \) or 36.8% as \( n \) becomes large. This is counterintuitive but mathematically optimal.

### Statistical Derivation

Given \( n \) options, the optimal strategy is to wait until a certain fraction of options have been observed before making a selection. This 'wait' fraction is derived from the probability maximization principle, leading to the \( 1/e \) rule. This is because the expected maximum of a uniformly distributed set occurs at the \( 1/e \) point.


## Statistical Derivation
Given \(n\) options, the probability of selecting the best one is maximized by observing the first \(n/e\) options and then choosing the next one that is better than all observed. The optimal stopping rule is derived from maximizing the probability, leading to \(1/e\) as the stopping fraction.

## Implementation and Usage
Ticket Secretary uses this principle to monitor ticket prices over time, advising when to buy based on historical price data and statistical analysis. The implementation involves:
- Data scraping for price trends.
- Applying the secretary problem algorithm to decide the purchase timing.
- Notifying the user to buy at the calculated optimal time.

## Authors

- Martin Elias Quintero, CEO guane Enterprises
- Jose M Munoz, MIT Physics PhD student
