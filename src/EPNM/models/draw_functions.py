import random
import numpy as np

def draw_function(param_dict, samples_dict):
    """
    Samples calibrated magnitudes of household demand/exogeneous demand shocks during the summer of 2021
    Performs global sensitivity analysis on other parameters
    """

    # Option 1
    # Shocks in/out
    param_dict['l1'] = np.random.normal(loc=7, scale=0.2*7)
    param_dict['l2'] = np.random.uniform(low=28, high=56)
    #Hiring and Firing speed
    param_dict['gamma_F'] = np.random.normal(loc=28, scale=0.2*28)
    param_dict['gamma_H'] = 2*param_dict['gamma_F']
    #Household savings and prospects
    param_dict['delta_S'] = np.random.uniform(low=0.5, high=1)
    param_dict['L'] = 1
    param_dict['b_s'] = 0.7
    #restock rate
    param_dict['tau'] =  np.random.normal(loc=14, scale=0.2*14)
    #Shocks lockdowns
    param_dict['l_s_1'] =  np.random.normal(loc=1, scale=0.075)*param_dict['l_s_1']
    param_dict['l_s_2'] =  np.random.normal(loc=1, scale=0.075)*param_dict['l_s_2']
    param_dict['c_s'] =  np.random.normal(loc=1, scale=0.075)*param_dict['c_s']
    param_dict['f_s'] =  np.random.normal(loc=1, scale=0.075)*param_dict['f_s']
    param_dict['c_s'] = np.where(param_dict['c_s'] > 1, 1, param_dict['c_s'])
    param_dict['f_s'] = np.where(param_dict['c_s'] > 1, 1, param_dict['c_s'])
    #Shocks summer 2020 
    param_dict['ratio_c_s'] =  np.random.uniform(low=0, high=1)
    param_dict['ratio_f_s'] =  np.random.uniform(low=0, high=1)

    return param_dict