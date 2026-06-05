# this is my function from utils
import numpy as np
from astroML.time_series import search_frequencies
# this is my function from utils - it needs to be imported from a .py file for
# processpoolexecutor to work.
def do_all(args):
    id, t, y, dy = args
    kwargs = dict(generalized=True)
    omega, power = search_frequencies(t, y, dy, n_eval=10000, n_retry=5, LS_kwargs=kwargs)
    
    idx_best = np.argmax(power)
    omega_best = omega[idx_best]
    power_best = power[idx_best]
    
    return [id, omega_best, power_best]