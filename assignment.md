
# Assignment - Statistics 2

In this assignment, you will explore Bayesian and Frequentist
approaches to estimate a sample statistics (proportion). In the Frequentist part, 
you will work on finding a point estimate with its confidence interval;
in the Bayesian part you will use Bayesian updating to calculate outcomes as 
a probabilistic distribution (posterior) based on a prior distribution and 
a likelihood function.

## Part 1: Frequentist Inference - Estimating the population proportion

In this first part, you will experiment with the Frequentist approach used 
to estimate a population proportion. For instance, you want to estimate the 
percentage of people that will vote to candidate A, or the percentage of women 
who have diabetes. In the Frequentist approach, we collect a sample from the 
population and then estimate the population proportion by computing the proportion 
of interest using the collected sample (sample proportion). More precisely, 
the following quantities are computed:

- Point Estimate:

   <img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\hat{p}&=\frac{\text{Total&space;number&space;of&space;specific&space;samples&space;}}{\text{Sample&space;size}}&space;\end{align*}" title="\begin{align*} \hat{p}&=\frac{\text{Total number of specific samples }}{\text{Sample size}} \end{align*}" />
     
- Standard Error:

   <img src="https://latex.codecogs.com/svg.latex?\begin{align*}&space;\sigma&space;&=&space;\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}&space;\end{align*}" title="\begin{align*} \sigma &= \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \end{align*}" />

- Critical Value:
   
   <img src="https://latex.codecogs.com/svg.latex?z" title="z" /> : associated with the desired confidence interval

The confidence interval is then defined as:

<img src="https://latex.codecogs.com/svg.latex?\hat{p}\pm&space;z&space;\cdot\sigma" title="\hat{p}\pm z \cdot\sigma" />

In this part of the assignment, we will use the sample proportion to estimate the head probability of a coin (`p(head)`). We denote the head probability by `p`.

1. Let's first use simulation to understand the interpretation of a confidence interval.

   a. Generate 200 random coin flips from a fair coin: `p(head)=0.5`. You can use `scipy.stats.bernoulli` as follows:
   
   ```python
   from scipy import stats
   dist = stats.bernoulli(0.5)
   flips = dist.rvs(200)
   ```
   
      Assume that 1 represents 'head' and '0' represents 'tail'.
      
      Using the generated sample, estimate the head probability and compute its corresponding 95% confidence interval. 
   
   b. Repeat the same experiment of the previous question for 1000 times. In each time, generate 200 random coin flips from a fair coin, find the 95% confidence interval and check if the true head probability (0.5) is in the confidence interval. How many times did you find that the true head probability is in the computed confidence interval?
   
   
2. You are now given a biased coin that you can find in [`src/coin.py`](src). The probability of head, unknown to you, is what you want to estimate. You can use the coin like this:

   ``` python   
    from coin import Coin
    mycoin = Coin()
    print (mycoin.flip())
    ```
   The `flip` method will return either `H` or `T`.

   a. Flip the coin for 500 times. Estimate the head probability and compute its corresponding 95% confidence interval.
   
      Save the obtained results of the coin flips (observations) because we will use them in the following question and in the second part.
      
   b. Now let's understand in which sense the point estimate: "sample proportion" is a good estimate. It can be shown that the sample proportion is the maximum likelihood estimate (MLE), i.e., it is the value under which the observed data is most likely to occur. Let's verify it using simulation by plotting the likelihood function of all observations:
   
   * Fill in the `coin_likelihood` function in [`src/functions.py`](src). It should take one observation (either 'H' or 'T') and the value for head probability `p` and return a value between 0 and 1. For example, if the data is 'H' and the value of `p` is 0.3, it should return 0.3. If the data is 'T' and the value of `p` is 0.3, it should return 0.7.
   
       The `coin_likelihood` function should be used like this:

        ```python
            coin_likelihood(single_data_point, p)
        ```
       Here, `single_data_point` means the result of one coin flip, and `p` means the value of head probability.
   
   * The likelihood function of the observations is viewed as a function defined over all possible values of `p` (head probability). Now `p` is a continuous non-negative value less than 1. To simulate and plot the likelihood function, we will consider a discrete set of values for `p`. Define a list or array that contains the possible values of `p` as follows: 0, 0.01, 0.02, ..., 0.99, 1. You can use `numpy.linspace`.
   
   * For each possible value of `p` defined in the previous question, compute the likelihood of all observations obtained in (2.a) (hint: multiply likelihood of each individual observation). Save the results in an array or list of likelihood values.
   
   * Plot the likelihood function of all observations vs the possible values for head probability. Which value of `p` maximizes the likelihood function? Is it close to the point estimate you found in (2.a)?

## Part 2: Bayesian Analysis -  Biased Coin

We now switch to the Bayesian approach. For the same data generated in part 1 question 2.a, we would like to estimate the head probability `p` of the biased coin.

In the Bayesian approach, we start with a prior that reflects our initial belief about the possible values for `p`. Then we continuously update our belief based on the observed data. Let's first setup the prior and define some functions.

1. **Prior**: We consider a uniform prior for `p`. Encode the prior as a dictionary: create a prior dictionary that has all the keys in 0, 0.01, 0.02, ..., 0.99, 1. The values of the dictionary should all be the same, as an equal probability of each of these keys occurring. You can use `numpy.linspace` to get the array of all the keys.


2. Fill in the [`normalize`](src/functions.py) function. It scales the values of the input dictionary `v` so that they sum to 1. To normalize, you need to find the sum of all the values of dictionary `v` and then divide each value by this sum.


3. Fill in the [`update`](src/functions.py) function. It should take one observation (i.e., the result of one coin flip), a dictionary prior and a likelihood function. This function should return the posterior probability: for each possible value of head probability (the keys of the dictionary prior), calculate the likelihood of the observation and multiply it with the prior value, make sure to call the normalize function as the final step!


4. Use each result of each coin flip generated in part 1 question 2.a to continuously update your belief about the possible values for head probability. Start with the uniform prior, pass the first coin flip to the `update` function, obtain a posterior and use this latter as your new prior when you consider the next coin flip result. Continue updating the prior until all coin flip results are used. On a single plot, overlay the initial uniform prior with the posteriors obtained after 1, 10, 50, 250 and 500 flips.


6. Use the final posterior to find the MAP (maximum a posteriori) estimate of the head probability, i.e., the value of `p` that maximizes the posterior probability. **Optional**: Find an approximation for the 95% credible interval.
