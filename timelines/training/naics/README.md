[Timelines ML](../../)

# Training Data for NAICS ML

We're creating a new Random Forest process infomed [by the prior ztca process](../../prep/all)

We'll use the state of Maine (MN) as our sample counties.  
We'll use NAICS level 2 which has about 72 industries.

Could we process the data entirely in Pandas rather then using SQLLite?

Yanqing is working on #1 and #2

### 1.) Prepare Python that loads naics4 data into Pandas for 2017 to 2021 for Maine

Source files. Load these directly from the URL into Pandas.

https://model.earth/community-data/industries/naics/US/counties/MN/US-MN-census-naics4-counties-2021.csv

View files on GitHub: [industries/naics/US/counties/MN](https://github.com/ModelEarth/community-data/tree/master/industries/naics/US/counties/MN)

---


### 2.) Output annual training files to:
output/2021/2021-naics2-counties.csv


For each industry, there will be 3 columns (Firms, People and Pay)

Fips, N1111-Firms, N1111-People, N1111-Pay, N2222-Firms, N2222-People, N2222-Pay, ...

Each row is a location (Fips = countyID) with 3 attributes per industry.

The following attribute names are equivalent:

Firms = Establishments
People = Employees
Pay = Payroll

As a reference, the prior structure for ztca (zipcode) was:

zcta, JobsTotal, JobsAgriculture, JobsEntertainment,…
Population, Poverty, PovertyUnder18, Education,WorkExperience, WorkingFulltime, WorkingFulltime_Poverty, y

Ronan is working on a similar pivot in [prep/industries](../../prep/industries/) for timelines, except the timeline rows are years.

---

### 3.)  Sijia - Append 0 or 1 to the last column.

Look at the prior process to document aspects to predict.

We can use county demographic attributes like education and poverty.

County demographic attributes can be fetched from the Google Data Commons API.

---
<br>

### 4.) Display results of Random Forest