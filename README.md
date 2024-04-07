# Ticket Secretary: Optimal Ticket Purchasing via the Secretary Problem

Ticket Secretary leverages a classic statistical theory to provide a smart, data-driven approach to purchasing tickets, aiming to save money and reduce the hassle in timing the purchase.

We coded it in a couple of hours, one of our for jokes  ;)

Ticket Secretary is a library that applies the secretary problem's statistical solution to optimize ticket purchasing for events like flights or concerts. It identifies the best time to buy tickets based on price trends and mathematical strategies.

## Secretary Problem in Depth
The secretary problem illustrates a scenario where one must choose the best option (e.g., secretary, ticket price) after seeing only a portion of the available choices. Mathematically, after reviewing \(e^{-1} \approx 37\%\) of the options, the next option better than all seen before is chosen. This strategy statistically provides the best chance of selecting the optimum choice.

## Statistical Derivation
Given \(n\) options, the probability of selecting the best one is maximized by observing the first \(n/e\) options and then choosing the next one that is better than all observed. The optimal stopping rule is derived from maximizing the probability, leading to \(1/e\) as the stopping fraction.

## Implementation and Usage
Ticket Secretary uses this principle to monitor ticket prices over time, advising when to buy based on historical price data and statistical analysis. The implementation involves:
- Data scraping for price trends.
- Applying the secretary problem algorithm to decide the purchase timing.
- Notifying the user to buy at the calculated optimal time.

## Authors

- Martin Elias, CEO guane Enterprises
- Jose M Munoz, MIT Physics PhD student
