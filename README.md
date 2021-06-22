# approximationIndex

Case study for the Jr. Trader position at SG Cap Trading.

Execute as:

`python3 approximate_index.py [n] .DJI dow_jones_historical_prices.csv > approximation.csv`

Market indexes often contain a large number of securities. For instance, the S&P 500 index contains 500 different stocks.

For many different reasons, we may wish to pick a small subset of these stocks which we believe would do a good job of replicating the behavior of the index as a whole.

Your project is to write a script that takes as input
- A number n of securities to pick
- Historical price data for each security in the index, as well as for the index itself

Produce as output a list of n of the index's constituents, along with the weightings, which you feel give a "good approximation" of the index's behavior. 

What constitutes as a "good approximation" is deliberately left open to interpretation. 

## Examples:

### n = 3

![n=3](https://user-images.githubusercontent.com/69542867/123009213-8624e300-d379-11eb-9fba-719f9df0b2c7.png)

### n = 10

![n=10](https://user-images.githubusercontent.com/69542867/123009217-87eea680-d379-11eb-9381-0b54e990efb4.png)

### n = 30

![n=30](https://user-images.githubusercontent.com/69542867/123009220-88873d00-d379-11eb-8938-8c3d45e42504.png)
