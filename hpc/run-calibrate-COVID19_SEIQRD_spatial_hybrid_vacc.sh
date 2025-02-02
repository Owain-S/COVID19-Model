#!/bin/bash
#PBS -N calibrate-COVID19_SEIQRD_spatial_stratified_vacc ## job name
#PBS -l nodes=1:ppn=18 ## single-node job, on 18 cores
#PBS -l walltime=72:00:00 ## max. 72h of wall time

# Define calibration settings
identifier="BASE"
agg="prov"
n_ag=10
n_pso=20
n_mcmc=5000
enddate="2021-10-07"

# Print job properties at the head of the stdout
echo "Spatial aggregation: ${agg}"
echo "Number of age groups: ${n_ag}"
echo "Number of PSO iterations: ${n_pso}"
echo "Number of MCMC iterations: ${n_mcmc}"
echo "Calibration enddate: ${enddate}"

# Change to package folder
cd $VSC_DATA/COVID19-Model/notebooks/calibration/

# Make script executable
chmod +x calibrate-COVID19_SEIQRD_spatial_hybrid_vacc.py

# Activate conda environment
source activate COVID_MODEL

# Add additional code to stop quadratic multiprocessing (tip from Balazs)
export OMP_NUM_THREADS=1

# Execute script. Note the python option -u to flush the prints to the stdout
python calibrate_CORE-COVID19_SEIQRD_spatial_hybrid_vacc.py -a ${agg} -n_ag ${n_ag} -n_pso ${n_pso} -n_mcmc ${n_mcmc} -e ${enddate} -ID ${identifier} -hpc

# Deactivate environment
conda deactivate
