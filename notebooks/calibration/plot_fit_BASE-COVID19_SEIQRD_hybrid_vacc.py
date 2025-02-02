"""
This script can be used to plot the model fit of the national COVID-19 SEIQRD model to the hospitalization data

Arguments:
----------
-ID:
    Identifier + aggregation level of the samples dictionary to be loaded.
-d:
    Date of calibration
-n_ag : int
    Number of age groups used in the model
-p : int
    Number of cores
-n : int
    Number of model trajectories used to compute the model uncertainty.
-k : int
    Number of poisson samples added a-posteriori to each model trajectory.
-s : 
    Save figures to results/calibrations/COVID19_SEIRD/national/others/

Example use:
------------
python plot_fit_BASE-COVID19_SEIQRD_hybrid_vacc.py -ID test -d 2023-02-15 -n_ag 10 -n 10 -k 1

"""

__author__      = "Tijs Alleman"
__copyright__   = "Copyright (c) 2023 by T.W. Alleman, BIOMATH, Ghent University. All Rights Reserved."

############################
## Load required packages ##
############################

import os
import sys
import datetime
import argparse
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from covid19_DTM.models.utils import initialize_COVID19_SEIQRD_hybrid_vacc
from covid19_DTM.data import sciensano
from covid19_DTM.visualization.output import _apply_tick_locator 
from covid19_DTM.models.utils import output_to_visuals
from covid19_DTM.models.utils import load_samples_dict

#############################
## Handle script arguments ##
#############################

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--agg", help="Spatial aggregation level (national, prov or arr)", default='national')
parser.add_argument("-ID", "--identifier", help="Calibration identifier")
parser.add_argument("-d", "--date", help="Calibration date")
parser.add_argument("-n_ag", "--n_age_groups", help="Number of age groups used in the model.", default = 10)
parser.add_argument("-n", "--n_samples", help="Number of samples used to visualise model fit", default=100, type=int)
parser.add_argument("-p", "--processes", help="Number of cpus used to perform computation", default=1, type=int)
parser.add_argument("-k", "--n_draws_per_sample", help="Number of binomial draws per sample drawn used to visualize model fit", default=1, type=int)
parser.add_argument("-s", "--save", help="Save figures",action='store_true')
args = parser.parse_args()

# Number of age groups used in the model
age_stratification_size=int(args.n_age_groups)

################################
## Define simulation settings ##
################################

# Start and end of simulation
end_sim = datetime(2022,1,1)
# Confidence level used to visualise model fit
conf_int = 0.05

##############################
## Define results locations ##
##############################

# Path where figures and results should be stored
fig_path = f'../../results/covid19_DTM/calibrations/{str(args.agg)}/others/WAVE2/'
# Path where MCMC samples should be saved
samples_path = f'../../data/covid19_DTM/interim/model_parameters/calibrations/{str(args.agg)}/'
# Verify that the paths exist and if not, generate them
for directory in [fig_path, samples_path]:
    if not os.path.exists(directory):
        os.makedirs(directory)

#############################
## Load samples dictionary ##
#############################

samples_dict = load_samples_dict(samples_path+str(args.agg)+'_'+str(args.identifier) + '_SAMPLES_' + str(args.date) + '.json', age_stratification_size=age_stratification_size)
warmup = samples_dict['warmup']
# Start of calibration warmup and beta
start_calibration = datetime.strptime(samples_dict['start_calibration'], '%Y-%m-%d')
start_sim = start_calibration
# Last datapoint used to calibrate warmup and beta
end_calibration = datetime.strptime(samples_dict['end_calibration'], '%Y-%m-%d')
# Overdispersion data
dispersion = float(samples_dict['dispersion'])

##################################################
## Load data not needed to initialize the model ##
##################################################

# Sciensano hospital and vaccination data
df_hosp, df_mort, df_cases, df_vacc = sciensano.get_sciensano_COVID19_data(update=False)
df_hosp = df_hosp.groupby(by=['date']).sum()
df_cases = df_cases.groupby(by=['date']).sum()
# Serological data
df_sero_herzog, df_sero_sciensano = sciensano.get_serological_data()
# Deaths in hospitals
df_sciensano_mortality = sciensano.get_mortality_data()
deaths_hospital = df_sciensano_mortality.xs(key='all', level="age_class", drop_level=True)['hospital','cumsum']

##########################
## Initialize the model ##
##########################

model, BASE_samples_dict, initN = initialize_COVID19_SEIQRD_hybrid_vacc(age_stratification_size=age_stratification_size, update_data=False, stochastic=True,
                                                                        start_date=start_calibration)
model.parameters['beta'] = samples_dict['beta']

#######################
## Sampling function ##
#######################

from covid19_DTM.models.draw_functions import draw_fnc_COVID19_SEIQRD_hybrid_vacc as draw_fcn

#########################
## Perform simulations ##
#########################

print('\n1) Simulating COVID19_SEIQRD_hybrid_vacc '+str(args.n_samples)+' times')

start_sim = start_calibration
out = model.sim([start_sim, end_sim],warmup=warmup,N=args.n_samples,draw_function=draw_fcn,samples=samples_dict, processes=int(args.processes))
df_2plot = output_to_visuals(out, ['M_in','H_in', 'H_tot', 'ICU_R', 'ICU_D', 'C_icurec', 'S', 'R', 'D'], alpha=dispersion, n_draws_per_sample=args.n_draws_per_sample, UL=1-conf_int*0.5, LL=conf_int*0.5)
simtime = out['date'].values



#######################
## Visualize results ##
#######################

print('2) Visualizing fit')

fig,(ax1,ax2,ax3,ax4,ax5) = plt.subplots(nrows=5,ncols=1,figsize=(8.3,11.7),sharex=True)

# Plot mildly sick
ax1.plot(df_2plot['M_in','mean'], color='blue', linewidth=1.5)
ax1.fill_between(simtime, df_2plot['M_in','lower'], df_2plot['M_in','upper'],alpha=0.20, color = 'blue')
ax1.scatter(df_cases[start_calibration:end_sim].index,df_cases[start_calibration:end_sim], color='black', alpha=0.20, linestyle='None', facecolors='black', s=10)
ax1 = _apply_tick_locator(ax1)
ax1.set_xlim(start_sim,end_sim)
ax1.set_ylabel('Incidence\nMild cases (-)', fontsize=13)
ax1.get_yaxis().set_label_coords(-0.1,0.5)
ax1.grid(False)
# Plot hospitalizations
ax2.plot(df_2plot['H_in','mean'], color='blue', linewidth=1.5)
ax2.fill_between(simtime, df_2plot['H_in','lower'], df_2plot['H_in','upper'],alpha=0.20, color = 'blue')
ax2.scatter(df_hosp[start_calibration:end_calibration].index,df_hosp['H_in'][start_calibration:end_calibration], color='red', alpha=0.2, linestyle='None', facecolors='red', s=10)
ax2.scatter(df_hosp[pd.to_datetime(end_calibration)+timedelta(days=1):end_sim].index,df_hosp['H_in'][pd.to_datetime(end_calibration)+timedelta(days=1):end_sim], color='black', alpha=0.2, linestyle='None', facecolors='black', s=10)
ax2 = _apply_tick_locator(ax2)
ax2.set_xlim(start_sim,end_sim)
ax2.set_ylabel('Incidence\nHospital (-)', fontsize=13)
ax2.get_yaxis().set_label_coords(-0.1,0.5)
ax2.grid(False)
# Plot hospital total
ax3.plot(simtime, df_2plot['H_tot', 'mean'], color='blue', linewidth=1.5)
ax3.fill_between(simtime, df_2plot['H_tot', 'lower'], df_2plot['H_tot', 'upper'], alpha=0.20, color = 'blue')
ax3.scatter(df_hosp[start_calibration:end_sim].index,df_hosp['H_tot'][start_calibration:end_sim], color='black', alpha=0.2, linestyle='None', facecolors='black', s=10)
ax3 = _apply_tick_locator(ax3)
ax3.set_ylabel('Load\nHospital (-)', fontsize=13)
ax3.get_yaxis().set_label_coords(-0.1,0.5)
ax3.grid(False)
# Plot ICU
ax4.plot(simtime, df_2plot['ICU_R', 'mean']+df_2plot['ICU_D', 'mean']+df_2plot['C_icurec', 'mean'], color='blue', linewidth=1.5)
ax4.fill_between(simtime, df_2plot['ICU_R', 'lower']+df_2plot['ICU_D', 'lower']+df_2plot['C_icurec', 'lower'], df_2plot['ICU_R', 'upper']+df_2plot['ICU_D', 'upper']+df_2plot['C_icurec', 'upper'], alpha=0.20, color = 'blue')
ax4.scatter(df_hosp[start_calibration:end_sim].index,df_hosp['ICU_tot'][start_calibration:end_sim], color='black', alpha=0.2, linestyle='None', facecolors='black', s=10)
ax4 = _apply_tick_locator(ax4)
ax4.set_ylabel('Load\nIntensive Care (-)', fontsize=13)
ax4.get_yaxis().set_label_coords(-0.1,0.5)
ax4.grid(False)
# Plot fraction of immunes
ax5.plot(df_2plot['R','mean'][start_calibration:'2021-03-01']/sum(initN)*100, color='blue', linewidth=1.5)
ax5.fill_between(simtime, df_2plot['R','lower']/sum(initN)*100, df_2plot['R','upper']/sum(initN)*100,alpha=0.20, color = 'blue')
yerr = np.array([df_sero_herzog['rel','mean']*100 - df_sero_herzog['rel','LL']*100, df_sero_herzog['rel','UL']*100 - df_sero_herzog['rel','mean']*100 ])
ax5.errorbar(x=df_sero_herzog.index,y=df_sero_herzog['rel','mean'].values*100,yerr=yerr, fmt='x', color='black', elinewidth=1, capsize=5)
yerr = np.array([df_sero_sciensano['rel','mean']*100 - df_sero_sciensano['rel','LL']*100, df_sero_sciensano['rel','UL']*100 - df_sero_sciensano['rel','mean']*100 ])
ax5.errorbar(x=df_sero_sciensano.index,y=df_sero_sciensano['rel','mean']*100,yerr=yerr, fmt='^', color='black', elinewidth=1, capsize=5)
ax5.legend(['model (mean)', 'model (95% CI)', 'Herzog et al. 2020', 'Sciensano'], loc='upper right', fontsize=13)
ax5.axvline(x=pd.Timestamp('2020-12-27'), linewidth=1.5, linestyle='--', color='black')
ax5 = _apply_tick_locator(ax5)
ax5.set_xlim(start_sim,end_sim)
ax5.set_ylim(0,35)
ax5.set_ylabel('Seroprelevance (%)', fontsize=13)
ax5.get_yaxis().set_label_coords(-0.1,0.5)
ax5.grid(False)

plt.tight_layout()
plt.show()
if args.save:
    fig.savefig(fig_path+args.filename[:-5]+'_FIT.pdf', dpi=300, bbox_inches='tight')
    fig.savefig(fig_path+args.filename[:-5]+'_FIT.png', dpi=300, bbox_inches='tight')
plt.close()

print('3) Visualizing fit on deaths')

dates = ['2020-07-01', '2021-01-01', '2021-07-01']

fig,axes = plt.subplots(nrows=len(dates),ncols=1,figsize=(14,4*len(dates)),sharex=True)
if len(dates) == 1:
   axes = [axes,]

for idx,date in enumerate(dates):
   data_sciensano = []
   for jdx,age_group in enumerate(df_sciensano_mortality.index.get_level_values(0).unique().values[1:]):
       data_sciensano.append(df_sciensano_mortality.xs(key=age_group, level="age_class", drop_level=True).loc[dates[idx]]['hospital','cumsum'])
    
   axes[idx].scatter(df_sciensano_mortality.index.get_level_values(0).unique().values[1:],out['D'].mean(dim='draws').sum(dim='doses').loc[dict(date=date)],color='black',marker='v',zorder=1)
   yerr = np.zeros([2,len(out['D'].quantile(dim='draws',q=0.975).loc[dict(date=date)].values)])
   yerr[0,:] = out['D'].mean(dim='draws').sum(dim='doses').loc[dict(date=date)] - out['D'].sum(dim='doses').quantile(dim='draws',q=0.025).loc[dict(date=date)].values
   yerr[1,:] = out['D'].sum(dim='doses').quantile(dim='draws',q=0.975).loc[dict(date=date)].values - out['D'].mean(dim='draws').sum(dim='doses').loc[dict(date=date)]
   axes[idx].errorbar(x=df_sciensano_mortality.index.get_level_values(0).unique().values[1:],
                      y=out['D'].sum(dim='doses').mean(dim='draws').loc[dict(date=date)],
                      yerr=yerr,
                      color = 'black', fmt = '--v', zorder=1, linewidth=1, ecolor='black', elinewidth=1, capsize=5)
   axes[idx].bar(df_sciensano_mortality.index.get_level_values(0).unique().values[1:],data_sciensano, width=1,alpha=0.7,zorder=0)
   axes[idx].set_xticklabels(['[0,12(','[12,18(','[18,25(','[25,35(','[35,45(','[45,55(','[55,65(','[65,75(','[75,85(','[85,120('])
   axes[idx].set_ylabel('Cumulative\nHospital deaths')
   axes[idx].set_title(date)
   axes[idx].grid(False)
plt.show()
if args.save:
   fig.savefig(fig_path+args.filename[:-5]+'_DEATHS.pdf', dpi=300, bbox_inches='tight')
   fig.savefig(fig_path+args.filename[:-5]+'_DEATHS.png', dpi=300, bbox_inches='tight')

##########################################
## Save a copy of the simulation result ##
##########################################

print('4) Save a copy of the simulation output')
# Path where the xarray should be stored
file_path = f'../../data/covid19_DTM/interim/model_parameters/initial_conditions/national/'
out.coords.update({'Nc': range(len(out.coords['Nc']))})
out.mean(dim='draws').to_netcdf(file_path+str(args.agg)+'_'+str(args.identifier)+'_SIMULATION_'+ str(args.date)+'.nc')

# Work is done
sys.stdout.flush()
sys.exit()