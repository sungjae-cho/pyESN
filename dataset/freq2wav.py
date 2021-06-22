import numpy as np

def frequency_generator(N,min_period,max_period,n_changepoints,randomstate):
    """returns a random step function with N changepoints
       and a sine wave signal that changes its frequency at
       each such step, in the limits given by min_ and max_period."""

    if n_changepoints == 0:
        frequency_control = np.ones((N,1)) * randomstate.rand()
        periods = frequency_control * (max_period - min_period) + min_period
        frequency_output = np.zeros((N,1))
        z = 0
        for i in range(N):
            z = z + 2 * np.pi / periods[i]
            frequency_output[i] = (np.sin(z) + 1)/2
        return np.hstack([np.ones((N,1)),1-frequency_control]),frequency_output

    # vector of random indices < N, padded with 0 and N at the ends:
    changepoints = np.insert(np.sort(randomstate.randint(0,N,n_changepoints)),[0,n_changepoints],[0,N])
    # list of interval boundaries between which the control sequence should be constant:
    const_intervals = list(zip(changepoints,np.roll(changepoints,-1)))[:-1]
    # populate a control sequence
    frequency_control = np.zeros((N,1))
    for (t0,t1) in const_intervals:
        frequency_control[t0:t1] = randomstate.rand()
    # [OriginalCode] # periods = frequency_control * (max_period - min_period) + max_period
    periods = frequency_control * (max_period - min_period) + min_period
    # run time through a sine, while changing the period length
    frequency_output = np.zeros((N,1))
    z = 0
    for i in range(N):
        z = z + 2 * np.pi / periods[i]
        frequency_output[i] = (np.sin(z) + 1)/2
    return np.hstack([np.ones((N,1)),1-frequency_control]),frequency_output