def coin_likelihood(single_data_point, p):
    """
    Args:
        single_data_point (str): result of a signle coin flip ('H' or 'T')
        p  (int): head probability
    Returns:
        likelihood (float): the probability of the single_data_point given p.
    """
    pass  # fill in here




def normalize(v):
    '''
    Makes the sum of the probabilities values in dictionary v equal 1.

    Args: 
        v (dict): each key is a possible parameter value, each value 
                  is the associated non-normalized probability of 
                  that parameter value
    Returns: 
        normalized_v (dict): each key is a possible parameter value, each value 
                          is the associated normalized probability of 
                          that parameter value

    '''
    pass


def update(prior, likelihood_func, single_data_point):
    '''
    Conduct a bayesian update. For each possible parameter value
    in prior, multiply the prior probability by the likelihood
    of the single data point and return the posterior probability.

    Args:
        prior (dict): each key is a possible parameter value, each value 
                      is the associated normalized probability of 
                      that parameter value
                          
        single_data_point (str): a single observation (data point 'H' or 'T')
            
        likelihood_func (function): takes a new piece of data and a parameter
                                    value, outputs the likelihood of getting
                                    that data given that value of the parameter
                                        
            

    Returns:
        posterior (dict): each key is a possible parameter value, each value 
                          is the associated updated probability of 
                          that parameter value

    '''
    pass
