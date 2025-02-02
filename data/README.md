## Data sets for COVID-19 model

### Raw data sets

#### RESTORE

A folder containing all raw simulations used for the RESTORE reports, the reports are freely available at https://covid-en-wetenschap.github.io/restore.html

#### deaths

+ `DEMO_DEATH_OPEN.xlsx` contains total number of daily deaths per age class per arrondissement between 2009 and now. Current latest date: 21 February 2021. Data for 2020 and 2021 are not entirely complete yet. Downloaded from Statbel (https://statbel.fgov.be/nl/open-data/aantal-sterfgevallen-dag-geslacht-arrondissement-leeftijd)

#### Economic data

+ `input-output.xlsx` contains sectoral input-ouput tables for Belgium. Belgian data, NACE 64 classification. Retrieved from https://www.plan.be/databases/data-63-en-input_output_tables_2015
+ `Employees_NACE38.xlsx` contains the number of employees per sector from 2014 to 2018. Belgian data, NACE 38 classification. Retrieved from http://stat.nbb.be/?lang=nl, 'Bevolking en arbeidsmarkt' > 'Werkgelegenheid' > 'Binnenlands concept A38'.
+ `Employees_NACE64.xlsx` contains the number of employees per sector from 2014 to 2018. Belgian data, NACE 38 classification. Retrieved from http://stat.nbb.be/?lang=nl, 'Bevolking en arbeidsmarkt' > 'Werkgelegenheid' > 'Binnenlands concept A64'.
+ `table_ratio_inv_go.csv` contains, for every sector in the WIOD 55 classification, the number of days production can continue when no inputs are delivered (= stock). Retrieved from https://zenodo.figshare.com/articles/software/Production_networks_and_epidemic_spreading_How_to_restart_the_UK_economy_/12345527/1
+ `WIOD_shockdata.csv` contains estimated household and other demand shocks during an economic crisis. Retrieved from https://zenodo.figshare.com/articles/software/Production_networks_and_epidemic_spreading_How_to_restart_the_UK_economy_/12345527/1
+ `IHS_Markit_results_compact.csv` Criticality scores of IHS Markit analysts. The exact formulation of the question was as follows: “For each industry in WIOD 55, please rate whether each of its inputs are essential. We will present you with an industry X and ask you to rate each input Y. The key question is: Can production continue in industry X if input Y is not available for two months?” UK data, WIOD 55 classification. Retrieved from https://zenodo.figshare.com/articles/software/Production_networks_and_epidemic_spreading_How_to_restart_the_UK_economy_/12345527/1
+ `WoW Growths.xlsx` Contains on the datasheet `SECTORAL_WOW_GROWTHS` the week-over-week growth rate of B2B demand (or consumption) per NACE 21 sector (sectors A-U) from 2008 to 2021. Obtained by prof. Koen Schoors from an (to us) anonymuous bank.
+ `playing with shifts.xlsx` Contains the growth rate of B2B demand (or consumption) in number of weeks relative to the start of the second 2020 quarter. Here, -24 weeks means 24 weeks before the start of 2020Q2. This datasheet is a smoothed variant of the data in `WoW Growths.xlsx` using several filters. The data were made by Feliciaan De Palmenaer(feliciaan.depalmenaer@ugent.be or feliciaan.de.palmenaer@vub.be). Raw data obtained by prof. Koen Schoors from an (to us) anonymuous bank.
+ `ermg-tables.xlsx` Ecomical Risk Management Group (ERMG) business survey indicators. Series of surveys conducted by the ERMG to assess the economic impact of COVID-19. Retrieved from https://www.nbb.be/nl/ermg-enquetes 
+ `NBB_synthetic_GDP.xls` Synthetic GDP for different sectors, from 2020M2 until 2021M12. Retrieved from NBB stat.
+ `labor_supply_shock.csv` contains the ERMG employment survey from April 6th, 2020 and April 13th, 2020. Extracted from `data/covid19_DTM/raw/economical/ermg-tables.xlsx` tab `Organisation of employees`. Interpolations/extrapolations were made for the following NACE64 sectors: 2 (Forestry): identical to 01 and 03. 3 (mining) identical to 01, 02, 03. 16 (Manufacture of wood products): identical to 17. 18 (Printing and reproduction of recorded media): average of all manufacturing. 19 (Manufacture of coke and refined petroleum products): identical to 20. 27 (Manufacture of electrical equipment): identical to 28. 29 (Manufacture of motor vehicles): identical to 30. 33 (Repair and installation of machinery): average of all manufacturing. 35-36-37-38-39 (Electricity, gas, steam + Water supply): no labor supply shock. 45 (Wholesale, retail trade and repair of vehicles): identical to 46-47. 50 (Water transport): identical to 49. 53 (Postal services): identical to 49. M71-72-73-74-75 (Professional, scientific and technical activities): identical to 69-70. 77 (Rental and leasing): average of transport (49-50-51-52), manufacturing, agriculture, accomodation. 84 (Public administration): identical to 69-70. 85 (Education): consumer demand shock only. 86-87-88 (Human health and social work): no shock. 94 (Activities of membership organisations): consumer demand shock only. 95-96 (Repair of computers and household goods, other personal service activities): identical to 69-70. 97-98 (households as employers): consumer demand shock only.
+ `NAI_value_added.csv` contains the added value (per quarter) in the services during the COVID-19 pandemic, as published by the Institute for National Accounts. Raw data retrieved from: https://www.nbb.be/doc/ts/publications/economicreview/2021/ecorevii2021.pdf.

#### GIS

+ `NIS_name.csv` is a two way NIS-name table used for the function name2nis located in `src/models/utils.py`. It is a pandas dataframe with two columns: the first are the Belgian NIS codes, the second is the name corresponding to that NIS code.

+ `NIS_arrondissement.csv` : NIS-code of each arrondissement

+ `NIS_Province.csv` : NIS-code of each province

+ `arrondissements_per_province.csv` : province to which each arrondissement belongs

+ `inhabitants.csv` : number of inhabitants for each municipality, arrondissement and region  

+ `shapefiles/BE/...` :  shapefiles of Belgian municipalities, district, provinces, regions, arronddissements

+ `Postcode_Niscode` : dictionary that injectively relates postal codes and NIS codes.

#### Hospital data

+ `symptomOnsetHospitalization.xlsx` contains: 1) the date at which patients first reported having symptoms, 2) the data at which patients were hospitalized and 3) the age of the patient. Received from Ghent University hospital, contact: pascal.coorevits@uzgent.be .

+ `AZmariaMiddelares.xlsx` contains: 1) patient ID, 2) age and sex of patient, 3) per patient: in chronological order, from bottom to top (!), the amount of time spent in the emergency room, cohort or intensive care unit, 4) if the patient recovered or died. 'cohortafdeling D601' is a geriatric cohort ward, 'cohortafdeling D501' is a regular cohort ward. Received from AZ Maria Middelares, contact: Leen Van Hoeymissen (Leen.VanHoeymissen@AZMMSJ.BE).

+ `UZGent_full.xlsx` contains: 1) patient ID, 2) age and sex of patient, 3) per patient: the date of symptom onset, date of first assessment, date of first hospital contact, the admission date to the Ghent University hospital, the admission data to ICU, the discharge date in ICU, the discharge date from the Ghent University hospital. 5) if the patient recovered or died. Dataset received 05/07/2020 from the Ghent University Hospital, contact: prof. Ernst Rietzschel (ernst.rietzschel@ugent.be).

#### Interaction matrices

##### Willem 2012

+ `total.xlsx`, `home.xlsx`, `work.xlsx`, `leisure.xlsx`, `transport.xlsx`, `school.xlsx`, `otherplace.xlsx`:  contains the interaction matrix (in the place suggested by the spreadsheets name) based on a survey study in Flanders with 1752 participants. The spreadsheet has several tabs to distinguish between the nature and duration of the contact. The data were extracted using the social contact rates data tool made by Lander Willem, available at https://lwillem.shinyapps.io/socrates_rshiny/. For the extraction of the data, weighing by age, weighing by week/weekend were used and reciprocity was assumed. Contacts with non-household members are defined as leisure contacts instead of home contacts. 

##### CoMiX

+ `wave1.xlsx`, ..., `wave8.xlsx` : contain the interaction matrices under lockdown measures in Belgium. There is one spreadsheet per survey wave. The dates of the surveys were (wave 1 - 8): ['24-04-2020','08-05-2020','21-05-2020','04-06-2020','18-06-2020','02-07-2020','02-08-2020','02-09-2020'].  Each spreadsheet has two tabs to distinguish between the nature and duration of the contact. The data were extracted using a beta version of the social contact rates data tool made by Lander Willem, SOCRATES. The data are not yet publically available. For the extraction of the data, weighing by age, weighing by week/weekend were used and reciprocity was assumed.

#### Mobility
##### Google

+ `community_mobility_data_BE.csv` contains a copy of the Google Community Mobility Report dataset downloaded by the function `get_google_mobility_data()`. Mobility data is extracted from https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv?cachebust=2dcf78defb92930a Only data for Belgium is saved in `data/covid19_DTM/raw`, because the "global" file is over 250 Mb.

##### Apple
+ `apple_mobility_trends.csv` contains a copy of the Apple Mobility Trends downloaded by the function `get_apple_mobility_data()`. Mobility data is extracted from https://covid19-static.cdn-apple.com/covid19-mobility-data/2024HotfixDev12/v3/en-us/applemobilitytrends-2021-01-10.csv

##### Proximus
+ `outputPROXIMUS122747coronaYYYYMMDDAZUREREF001.csv`: complete origin-destination data saved on SFTP server and locally but NOT uploaded to GitHub.

#### Sciensano

+ `COVID19BE_HOSP.csv` contains a copy of the "HOSP" sheet from the publically available Sciensano data. Data is extracted from https://epistat.sciensano.be/Data/COVID19BE.xlsx
+ `COVID19BE_MORT.csv` contains a copy of the "MORT" sheet from the publically available Sciensano data. Data is extracted from https://epistat.sciensano.be/Data/COVID19BE.xlsx
+ `COVID19BE_CASES.csv` contains a copy of the "CASES_AGESEX" sheet from the publically available Sciensano data. Data is extracted from https://epistat.sciensano.be/Data/COVID19BE.xlsx
+ `COVID19BE_VACC.csv` contains a copy of the "VACC" sheet from the publically available Sciensano data. Data is extracted from https://epistat.sciensano.be/Data/COVID19BE.xlsx
+ `COVID19BE_VACC_MUNI_raw.csv` contains a copy of the "VACC_MUNI" sheet from the publically available Sciensano data. Data is extracted from https://epistat.sciensano.be/Data/COVID19BE.xlsx
+ `ObsInf.txt` contains cumulative observed infections from 1 March on
 (note that this is an underestimation since especially in the beginning, only sick people
   were tested)
+ `ObsDeceased.txt` contains cumulative observed deaths from 1 March on
+ `ObsRecovered.txt` contains cumulative observed recovered (from hospital) from 1 March on
+ `vacc_rescaling_values.csv` contains weekly rescaling values per NIS, per age, per effect (susc, inf, hosp), resulting from vaccination data. Calculated with Notebooks/preprocessing/MR-calculate-effective-rescalings.ipynb

#### Model parameters

+ `verity_etal.csv` contains age-stratified estimates of the number of symptomatic cases which result in hospitalization, the number of hospitalized patients in need of intensive care and the case fatality ratio (the percentage of individuals with symptomatic or confirmed disease who die from the disease). Data were obtained from https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(20)30243-7/fulltext
+ `davies_etal.csv` contains age-stratified estimates of the fraction of asymptomatic cases and relative susceptibility. Data were copied from https://www.nature.com/articles/s41591-020-0962-9
+ `others.csv` contains all other parameters used to run the model. Obtained from various sources, detailed in the report.

#### Belgian Census 2011

+ `Pop_LPW_NL_25FEB15.xlsx` contains the working population per sex, place of residence and place of work. First, the raw spreadsheet `data/covid19_DTM/raw/census_2011/Pop_LPW_NL_25FEB15.xlsx` was modified in MS Excel and placed in the data/covid19_DTM/interim folder under the name `Pop_LPW_NL_25FEB15_delete_unknown.xlsx`. Data free for download at https://census2011.fgov.be/download/downloads_nl.html.
+ `census_demo_nl_04nov14.xlsx` contains all demographic data from the 2011 Belgian census. From these data, the number of individuals in 10 year age-bins per Belgian arrondissement are calculated. The conversion notebook is `notebooks/0.1-twallema-extract-census-data.ipynb`.  Data free for download at https://census2011.fgov.be/download/downloads_nl.html .
+ `census_arbeidsmarkt_nl_24oct14.xlsx` contains all work related data from the 2011 Belgian census. Data free for download at https://census2011.fgov.be/download/downloads_nl.html .

#### QALY model

##### life_table_model

+ `Life_tables_Belgium.csv` contains belgiam life tables for different years and each gender. A copy containing only the necessary information for the most recent year (2019) was placed in the data/covid19_DTM/interim folder under the name: 'Life_table_Belgium_2019.csv'.  Data obtained from: https://statbel.fgov.be/nl/themas/bevolking/sterfte-en-levensverwachting/sterftetafels-en-levensverwachting .
+ `QoL_scores_Belgium_2018.csv` contains quality of life scores for the Belgian population calculated from the 2018 health survey under the EuroQOL 5 scale. The data was interpoletad to fit the main model's age bins and was placed in the data/covid19_DTM/interim under the name: 'QoL_scores_Belgium_2018_v1.cs'. Data obtained from: https://hisia.wiv-isp.be/SitePages/Home.aspx .
+ `De_Wilder_QoL_scores.xlsx` contains two datasheets: 1) QoL_scores, 2) prevalence_comorbidities. The QoL_scores sheet contains the quality-of-life (QoL) scores per number of chronical diseases in the Belgian population. The prevalence_comorbidities sheet contains a calculation of the chronical disease distribution of the Belgian population. Data obtained from Lisa Van Wilder.

##### long_COVID

+ `Long_COVID_prevalence.csv` contains the dynamical fraction of individuals reporting at least one symptom, up to 12 months post-COVID-19. For three severities of COVID-19: Mild, Moderate, Severe-Critical. Data extracted from: Wynberg et al. (2022) Evolution of coronavirus disease 2019 (covid-19) symptoms during the first 12 months after illness onset. 

##### postponement_non_covid_care

+ `hec03946-sup-0001-supplementary material.docx` contains supply-side cost-effectiveness thresholds and elasticities per disease group and age for the Netherlands. The data was used to estimate the cost per QALY gained per disease group. It was subsequently corrected for inflation, combined with costs of medical treatment and  and placed in data/covid19_DTM/interim folder under the name: 'hospital_data_qaly.xlsx'. Suplementary material of: Stadhouders, N., Koolman, X., Dijk, C., Jeurissen, P., and Adang, E. (2019). The marginal benefits of healthcare spending in the Netherlands: Estimating cost-effectiveness thresholds using a translog production function. Health Economics, 28(11):1331–1344.

###### Technische Cel voor de Verwerking van de Gegevens met betrekking tot de Ziekenhuizen

+ `download_20xx.xls` contains, for every disease group of the Major Diagnostic Groups (MDC), the total number of hospital stays in Belgium in year 20xx, as well as the total costs. Obtained from "Technische Cel voor de verwerking van de gegevensmet betrekking tot de ziekenhuizen": https://tct.fgov.be/webetct/etct-web/html/nl/index.jsp. 

###### UZG

`MZG 20XX.xlsx` contains for every patient hospitalized in the Ghent University Hospital during year 20XX the 1) Type of hospitalization, 2) Age of the patient (binned per 5 years age), 3) Date of hospitalization, date of hospital discharge, 4) Pathology (MDC classification). These data were obtained from the Ghent University Hospital (ethical advice BC-11147) and are confidential.

#### VOCs

+ `sequencing_501YV1_501YV2_501YV3.csv` contains the total number of sequenced samples and the number of samples of variants 501Y.V1 (British), 501Y.V2 (South African) and 501Y.V3 (Brazilian). Data available from week 49 of 2020 until week 14 of 2021. Data download from Tom Wenseleer's Git (https://github.com/tomwenseleers/newcovid_belgium); folder `~/data/2021_04_16/sequencing_501YV1_501YV2_501YV3.csv`.

#### Seroprelevance

+ `Belgium COVID-19 Studies - Sciensano_Blood Donors_Tijdreeks.csv` contains the overall seroprelevance in the Belgian population with confidence bounds. Downloaded from https://datastudio.google.com/embed/reporting/7e11980c-3350-4ee3-8291-3065cc4e90c2/page/R4nqB on 2021-04-19 by right clicking on a datapoint and selecting 'csv downloaden'.
+ `serology_covid19_belgium_round_1_to_7_v20210406.csv` contains the measured amount of antibodies of samples per province, per age group and in seven sampling waves. Downloaded from https://zenodo.org/record/4665373#.YH116nUzaV4 on 2021-04-19.

### Interim data sets conversion scripts

Conversion scripts are managed inside the `covid19model` package (`src/covid19model/data` folder).

#### RESTORE

`all_RESTORE_simulations.csv` contains all RESTORE predictions in a uniform format. The resulting .csv has a five-dimensional header: 1) author, 2) report version, 3) scenario, 4) hospital incidences or load, 5) statistic: mean, median, LL, UL. To load the .csv file correctly using pandas: `RESTORE_df = pd.read_csv(path_to_file+'all_RESTORE_simulations.csv', header=[0,1,2,3,4])`. Indexing is performed in the following way: `RESTORE_df['UGent','v7.0','S1','incidences','mean']` returns the daily hospitalizations (incidences) in scenario S1 of report v7.0 by UGent. The dataset was created by converting the raw RESTORE predictions using the script `~/notebooks/preprocessing/format-RESTORE-predictions.py`.

#### Hospital
+ `twallema_AZMM_UZG.xlsx` contains the merged dataset from AZ Maria Middelares and Ghent University hospital. The combined samplesize is 370 patients. The resulting dataset contains the following entries: 1) age of patient, 2) sex of patient, 3) type of stay. Emergency room only, Cohort only or ICU. Here, ICU implies that the patient spent a limited time in Cohort before transitioning to an ICU unit and if not deceased in ICU, the patient returns to Cohort for recovery, 4) outcome (R: recovered, D: deceased), 5) dC: time spent in a Cohort ward, 6) dICU: time spent in an ICU, 7) dICUrec: time spent in Cohort recovering after an ICU stay. Code of reformat performed in `~/notebooks/preprocesing/AZMM-UZG-hospital-data-analysis.py`.

#### Model parameters

+ `AZMM_UZG_hospital_parameters.csv` contains age-stratified estimates for the following model parameters: 1) c: probability of not going to an ICU where (1-c) is the probability of needing IC. 2) m0: mortality, given as a total (cohort + ICU) and separate for Cohort and ICU. 3) dC: average time spent in a Cohort ward if not going to ICU. Split in recovered and deceased. 4) dICU: average time spent in an ICU. Split in recovered and deceased. 4) dICU,rec: average length of recovery stay in Cohort after ICU. The analysis is performed using the script `~/notebooks/preprocessing/AZMM-UZG-hospital-data-analysis.py`.
+ `sciensano_hospital_parameters.csv` contains age-stratified estimates for the hospital parameters of the COVID19_SEIRD model. The analysis was performed using the script `~/notebooks/preprocessing/sciensano-hospital-data-analysis`. You must place the super secret detailed hospitalization dataset `COVID19BE_CLINIC.csv`in the same folder as this script in order to run it. Permission from Sciensano is needed to obtain the raw dataset.
+ `sciensano_bootstrap_fractions.npy` contains age-stratified bootstrapped samples for the cohort/ICU distribution and for the mortalities of the COVID19_SEIRD model. The analysis was performed using the script `~/notebooks/preprocessing/sciensano-hospital-data-analysis`. You must place the super secret detailed hospitalization dataset `COVID19BE_CLINIC.csv`in the same folder as this script in order to run it. Permission from Sciensano is needed to obtain the raw dataset.
+ `wu_asymptomatic_fraction.xlsx` contains the computation of the asymptomatic fraction of the Belgian population per age group based on a study of Wu, 2020 (https://www.nature.com/articles/s41591-020-0822-7/figures/2).


#### Belgian Census 2011
+ `Pop_LPW_NL_25FEB15_delete_unknown.xlsx`. First, the raw spreadsheet `data/covid19_DTM/raw/census_2011/Pop_LPW_NL_25FEB15.xlsx` was modified in MS Excel. The format of the data is as follows:
    - rows: municipality of residence
    - columns: municipality of work   
The dataset contained, for each Belgian province, a column of 'unknowns', indicating we know where these individuals live but not where they work. These 10 columns were removed manually. Further, the column `Werkt in Belgie` was renamed `Belgie` to make name-based row and column matching easier. The recurrent mobility matrix was extracted from these data. The conversion notebook is `notebooks/0.1-twallema-extract-census-data.ipynb`.
+ `recurrent_mobility.csv` contains a square recurrent mobility matrix of the Belgian arrondissements (43x43). The data were extracted from `Pop_LPW_NL_25FEB15_delete_unknown.xlsx`, the conversion was performed in `notebooks/0.1-twallema-extract-census-data.ipynb`. This data is deprecated since 2019.
+ `census-2011-updated_row-commutes-to-column_arrondissements.csv` contains a square (but non-symmetric) mobility matrix of the Belgian arrondissements (43x43). The data were extracted from `Pop_LPW_NL_25FEB15_delete_unknown.xlsx`.
+ `census-2011-updated_row-commutes-to-column_municipalities.csv` contains a square (but non-symmetric) mobility matrix of the Belgian municipalities (581x581). The data were extracted from `Pop_LPW_NL_25FEB15_delete_unknown.xlsx`.
+ `census-2011-updated_row-commutes-to-column_provinces.csv` contains a square (but non-symmetric) mobility matrix of the Belgian provinces *and* arrondissement Brussels-Capital (NIS 21000) (11x11). The data were extracted from `Pop_LPW_NL_25FEB15_delete_unknown.xlsx`.
+ `census-20110-updated_row-commutes-to-column_test.csv` contains a square (but non-symmetric) mobility matrix of the three Belgian arrondissements (Antwerpen, Brussel, Gent) (3x3). This is an artificial case: all commuters that leave the home arrondissement but do *not* go to one of the other two arrondissements, have been counted as staying at the home arrondissement instead. The data were extracted from `Pop_LPW_NL_25FEB15_delete_unknown.xlsx`.

#### QALY model

##### life_table_model

+ `Life_table_Belgium_2019.csv` contains the death rate (mu_x) at a given age for the Belgian population as of 2019. Extracted from `data/covid19_DTM/raw/QALY_model/life_table_model/Life_tables_Belgium.xls`.
+ `QoL_scores_Belgium_2018_v3.csv` contains age-stratified quality-of-life scores for the Belgian population calculated from the 2018 health survey under the EuroQOL 5 scale.
+ `De_Wilder_QoL_scores.xlsx` contains three datasheets: 1) QoL_scores, 2) prevalence_comorbidities and 3) SMR. The QoL_scores sheet contains the quality-of-life (QoL) scores per number of chronical diseases, extrapolated from `data/covid19_DTM/raw/QALY_model/core/De_Wilder_QoL_scores.xlsx` into the ten nine-year age-strata of the BIOMATH COVID-19 SEIQRD model. The prevalence_comorbidities sheet contains the chronical disease distribution of the Belgian population, extrapolated from the distribution in `data/covid19_DTM/raw/QALY_model/core/De_Wilder_QoL_scores.xlsx` into the ten nine-year age-strata of the BIOMATH COVID-19 SEIQRD model. The column `rel_risk_Charlson` comes from the following study by Charlson et. al, 1994 (https://pubmed.ncbi.nlm.nih.gov/7722560/). The column `weighted_sum` contains the weighted sums of the average comorbidity profile with the `rel_risk_Charlson`. The `SMR` sheet contains an estimate of the "Standardized Mortality Ratio" per age group and is obtained by scaling the `rel_risk_Charlson` column with the `weighted_sum` column in the `prevalence_comorbidities` sheet.

##### long_COVID

+ `average_QALY_losses.csv` Contains the total number of QALYs lost to long-COVID upon infection at age `x in [0, 105]` for the following COVID-19 severities: 1) Non-hospitalised (with AD), 2) Non-hospitalised (no AD), 3) Cohort, 4) IC. Computed using the script `path/to/script`.

##### Postponement of non-COVID-19 care

+ `hospital_stays_costs_BE.xlsx` contains a formatted version of the files found in `data/covid19_DTM/raw/QALY_model/postponement_non_covid_care/technische_cel_verwerking _gegevens_ziekenhuizen`. Contains two sheets: 1) The number of hospital stays in Belgium, 2) The total costs of treatment in Belgium. Data from 2017, 2018, 2019 are averaged as a baseline. Data from 2020 are compared to the baseline. The number of treatments was reduced with 9% in 2020.

+ `hospital_yearly_QALYs.xlsx` contains from the mean, lower and upper estimates of the Willingness-to-Pay threshold (WTP) and elasticity per disease group found in `data/covid19_DTM/raw/QALY_model/postponement_non_covid_care/hec03946-sup-0001-supplementary material.docx`. Contains the yearly costs given to hospital treatment in Belgium, averaged 2017-2019, from `data/covid19_DTM/interim/QALY_model/postponement_non_covid_care/hospital_stays_costs_BE.xlsx`. These data are used to compute the yearly number of QALYs gained in Belgium by treating these diseases: `QALYs = Cost/(-elasticity*WTP)`.

###### UZG

These data are confidential.

+ `MZG_2016_2021.csv` contains the absolute number of patients present in the Ghent University Hospital per Major Diagnostic Group from 2016 to 2021.
+ `2020_2021_normalized.csv` contains the number of treated patients per Major Diagnostic Group during the 2020-2021 COVID-19 pandemic, normalized with the prepandemic baseline.

#### Sciensano

+ `clusters.csv` contains the number of clusters traced back to 1) families, 2) WZCs, 3) schools, 4) workplaces and 5) others over the period 2020-12-28 until 2021-02-21. Data extracted from the weekly Sciensano reports, available at https://covid-19.sciensano.be/nl/covid-19-epidemiologische-situatie. Last visited 2021-03-31.
+ `sciensano_detailed_mortality.csv` contains the number of deaths (incidence and cumulative number) per age group, in total, in hospitals and in nursing homes. Since our model does not predict nursing home deaths, model output must be compared to deaths in hospitals. Data conversion was done using the script` ~/notebooks/preprocessing/sciensano-mortality-data-analysis.py`. You must place the super secret detailed hospitalization dataset `COVID19BE_MORT_RAW.csv` in the same folder as this script in order to run it. Permission from Sciensano is needed to obtain the raw dataset.
+ `COVID19BE_VACC_MUNI_format_{agg}.csv` contains the formatted number of (first) vaccine doses per week, per geographical aggregation and per age group in a pandas dataframe with three-level multiindex.

#### Demographic data

+ `age_structure_per_arrondissement.csv` : population of each age per arrondissement. Most likely retrieved from Statbel: https://bestat.statbel.fgov.be/bestat/crosstable.xhtml?datasource=65ee413b-3859-4c6f-a847-09b631766fa7. 

+ `age_structure_per_municipality.csv` : population of each age per municipality. Most likely retrieved from Statbel: https://bestat.statbel.fgov.be/bestat/crosstable.xhtml?datasource=65ee413b-3859-4c6f-a847-09b631766fa7.

+ `age_structure_per_province.csv` : population of each age per province. Most likely retrieved from Statbel: https://bestat.statbel.fgov.be/bestat/crosstable.xhtml?datasource=65ee413b-3859-4c6f-a847-09b631766fa7.

+ `area_arrond.csv` contains the area of Belgian arrondissements per NIS code in square meters.

+ `area_municip.csv` contains the area of Belgian municipalities per NIS code in square meters.

+ `area_province.csv` contains the area of Belgian provinces per NIS code in square meters.

+ `area_test.csv` contains the area of arrondissements Antwerp, Brussels, Gent.

#### Economic data

##### Model parameters

All economic data from the data/covid19_DTM/raw/economical was converted using the script `notebooks/preprocessing/extract-economic-data.py`. Missing raw datasets are downloaded automatically, except for those of the Belgian National Bank.

+ `conversion_matrices.xlsx` contains conversion matrices to more easily aggregate data from different sector classifications. F.i. converting from NACE 64 to WIOD 55 classification.
+ `other_parameters.csv` contains the sectoral output during business-as-usual, household demand during business-as-usual, other final demand during business-as-usual, the desired stock, consumer demand shock, other demand shock, sectoral employees during business-as-usual and sectoral employees under lockdown. Data from various sources. NACE 64 classification.
+ `IO_NACE64.csv` contains the input-output table for Belgium, formatted to NACE 64 classification.
+ `IHS_critical_NACE64.csv` contains the IHS Market Analysts data, reformatted from WIOD 55 to the NACE 64 classification. Columns represent the critical inputs to a sector. Dependecy of L68 (real estate) on H53 (Postal services) was removed. The Real estate sector did not face a big decline in economic activity, as detailed in https://www.nbb.be/doc/ts/publications/economicreview/2021/ecorevii2021.pdf (chart 5). Dependecy of H49 (Land Transport) and H51 (Air Transport) on I55-56 (Accodomodation) was removed as the closure of Accomodation during the lockdown led to overly large declines in economic activity. Sector Rental and Leasing (N77) critically depends on C33 (Repair of Machinery) and G45 (Retail of vehicles) only. Travel agencies (N79) critically depend on Air, Water and Land transport (H49/H50/H51) and importantly depend on I55-56, N77/N78. All dependencies of Public Administration (O84) and Education (P85) were relaxed as the government sector didn't face any shocks during the COVID-19 pandemic (https://www.nbb.be/doc/ts/publications/economicreview/2021/ecorevii2021.pdf).
+ `labor_supply_shock.csv` contains the ERMG employment survey from April 6th, 2020 and April 13th, 2020. Extracted from `data/covid19_DTM/raw/economical/ermg-tables.xlsx` tab `Organisation of employees`. Shocks were only applied to sectors facing mandatory closure (manufacturing, recreation, retail). Interpolations/extrapolations were made for the following NACE64 sectors: 2 (Forestry): identical to 01 and 03. 3 (mining) identical to 01, 02, 03. 16 (Manufacture of wood products): identical to 17. 18 (Printing and reproduction of recorded media): average of all manufacturing. 19 (Manufacture of coke and refined petroleum products): identical to 20. 27 (Manufacture of electrical equipment): identical to 28. 29 (Manufacture of motor vehicles): identical to 30. 33 (Repair and installation of machinery): average of all manufacturing. 35-36-37-38-39 (Electricity, gas, steam + Water supply): no labor supply shock. 45 (Wholesale, retail trade and repair of vehicles): identical to 46-47. 50 (Water transport): identical to 49. 53 (Postal services): identical to 49. M71-72-73-74-75 (Professional, scientific and technical activities): identical to 69-70. 77 (Rental and leasing): average of transport (49-50-51-52), manufacturing, agriculture, accomodation. 84 (Public administration): identical to 69-70. 85 (Education): consumer demand shock only. 86-87-88 (Human health and social work): no shock. 94 (Activities of membership organisations): consumer demand shock only. 95-96 (Repair of computers and household goods, other personal service activities): identical to 69-70. 97-98 (households as employers): consumer demand shock only.
+ `demand_shock.csv` contains the exogeneous and consumer demand shocks under lockdown measures.

##### Calibration data

+ `ERMG_temporary_unemployment.xlsx` contains the percentage temporary unemployed during the pandemic in different sectors. Data were converted in MS Excel from tab `Organisation of employees` in `/data/covid19_DTM/raw/economical/ermg-tables.xlsx`. Data for 'Consultancy/Engineering services' averaged and assigned to NACE 69-70. 'Liberal professions' and 'Cleaning and security services' averaged and assigned to NACE 80-82. 'Retail sales (food)'and 'Retail sales (non-food)' averaged and assigned to NACE 47.
+ `ERMG_revenue.xlsx` contains the self-reported revenue decline during the pandemic in different sectors. Data were converted in MS Excel from tab `Revenue impact current week` in `/data/covid19_DTM/raw/economical/ermg-tables.xlsx`. Data for 'Consultancy/Engineering services' averaged and assigned to NACE 69-70. 'Liberal professions' and 'Cleaning and security services' averaged and assigned to NACE 80-82. 'Retail sales (food)'and 'Retail sales (non-food)' averaged and assigned to NACE 47.
+ `NBB_synthetic_GDP.xlsx` contains the synthetic GDP curves for some NACE 64 sectors. Data converted in MS Excel from `data/covid19_DTM/raw/economical/NBB_synthetic_GDP.xlsx`.
+ `WoW Growths.xlsx` Contains on the datasheet `SECTORAL_GROWTHS_ABS` the absolute B2B demand per NACE 21 sector from 2008 to 2021. Contains on the datasheet `SECTORAL_GROWTHS_REL` the relative B2B demand per NACE 21 sector from 2008 to 2021, as compared per year/week with the average B2B demand of the three previous years. Contains on the datasheet `SECTORAL_GROWTHS_REL_100` the relative B2B demand per NACE 21 sector from 2008 to 2021, as compared per year/week with the average B2B demand of the three previous years. But, all values are normalised with the average of the first three observations in `SECTORAL_GROWTHS_REL` to make sure all timeseries start around 100%. Converted in MS Excel starting from the dataset of the same name in the raw data folder.
+ `NAI_value_added.csv` contains the added value (per quarter) in the services during the COVID-19 pandemic, as published by the Institute for National Accounts. Raw data retrieved from: https://www.nbb.be/doc/ts/publications/economicreview/2021/ecorevii2021.pdf. Data for sectors O-P/Q was merged using the weighted average gross value added (model state `x`). Data were merged to obtain O-P-Q from the NACE10 classification. Converted in MS Excel.

#### mobility

Note: only saved locally and on S-drive (not on Git due to NDA). Contains processed origin-destination matrices at the level of municipalities, arrondissements and provinces:
+ staytime: `fractional-mobility-matrix_staytime_*_*.csv`: origin-destination matrices in terms of estimated length of stay, normalised over the total available time. Subtracted 8 hours of sleep per day, and corrected for the GDPR-protected -1 values
+ baseline: `fractional-mobility-matrix_staytime_arr_baseline-*.csv`: normalised origin-destination matrix for three distinct periods: business days, weekends and vacation days. These may be used to distinguish how many additional people were forced to stay at home, and/or to estimate the goal of travel (work/leisure/...)

#### seroprelevance

+ `sero_national_stratified_own` contains for every of the seven sampling waves and for 10 age groups the mean and 95% confidence interval on the seroprelevance of SARS-CoV-2 IGG antibodies. This dataset is made by analysing `~/data/covid19_DTM/raw/sero/serology_covid19_belgium_round_1_to_7_v20210406.csv` using the script `~/notebooks/preprocessing/herzog-sero-data-analysis.py`. Currently, the positive samples are unweighted, the analysis is performed on the national level and the analysis does not account for the test sensitivity and specificity.
+ `sero_national_overall_herzog.csv` contains for every of the seven sampling waves, the non age-stratified seroprelevance in the Belgian population. Copied from table S1 in the manuscript of Sereina Herzog, available on Medrxiv: https://www.medrxiv.org/content/10.1101/2020.06.08.20125179v5.full-text.
+ `table_S1_Herzog.docx` contains table S1 from the manuscript of Sereina Herzog, available on Medrxiv: https://www.medrxiv.org/content/10.1101/2020.06.08.20125179v5.full-text.

### simulated

Contains zarr directories, which in turn contain groups that each hold a different simulation result. The aim of this 'simulation database' is to be able to save simulation results and perform post-processing without always having to go through the long and computationally demanding task of simulating (using the base.py sim function). This is especially relevant for spatially stratified SEIRD extended models, as these typically take G times longer to run (where G is the level of spatial stratification).

Simulations are saved here using the `utils.py` function `save_sim()` and opened using the `open_sim()` function. The content of the simulations is suggested in the directory titles and mentioned in the 'description' attribute of the zarr groups. It is also printed upon opening the simulation with `open_sim()`. Additionally, the simulation is quickly described here as well.

#### Sanity-check_100sims_100days_Nctot-to-Nchome-day40.zarr

+ `arr_1E-per-arr` description: "Stochastic spatial SEIRD extended model with 100 parallel simulations in 43 arrondissements over 100 days.At day 0 a single exposed person in the age class 30-40 is released ineach of the arrondissements. At day 40 measures are imposed, bringing down the contact rate from Nc_total to Nc_home over the course of 5 + 5 days (tau and l compliance parameters) reaches full effect."