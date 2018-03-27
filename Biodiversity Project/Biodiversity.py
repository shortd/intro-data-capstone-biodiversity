
# coding: utf-8

# In[2]:


import codecademylib
#solely for codecademy
import pandas as pd
#pandas is is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
from matplotlib import pyplot as plt
# Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

# Loading the Data
species = pd.read_csv('species_info.csv')

print species.head(5)
#.head() prints just the first few rows of data – you can specify how many rows you want to see.

species_count = species.scientific_name.nunique()

species_type = species.category.unique()

conservation_statuses = species.conservation_status.unique()

#nunique() versus unique() = nun returns a number where as un returns a list of unique strings.

conservation_counts = species.groupby('conservation_status').scientific_name.nunique().reset_index()

#lists by string “conservation status” with a number of each (nunique())
#reset_index() makes a new index (or primary key column)

species.fillna('No Intervention', inplace = True)
#fillna replaces a ‘nan’ with whatever string argument you want.

conservation_counts_fixed = species.groupby('conservation_status').scientific_name.nunique().reset_index()
print conservation_counts_fixed


import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'
print(species.head(45))

category_counts = species.groupby(['category','is_protected']).scientific_name.nunique().reset_index()

print(category_counts.head())

category_pivot = category_counts.pivot(columns = 'is_protected', index = 'category', values = 'scientific_name').reset_index()
print(category_pivot)


import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'
#print(species.head(45))

category_counts = species.groupby(['category','is_protected']).scientific_name.nunique().reset_index()

#print(category_counts.head())

category_pivot = category_counts.pivot(columns = 'is_protected', index = 'category', values = 'scientific_name').reset_index()

category_pivot.columns = ['category', 'not_protected', 'protected']
category_pivot['percent_protected'] = (category_pivot.protected/(category_pivot.protected+category_pivot.not_protected))*100
print(category_pivot)



import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

# Loading the Data
species = pd.read_csv('species_info.csv')

# print species.head()

# Inspecting the DataFrame
species_count = len(species)

species_type = species.category.unique()

conservation_statuses = species.conservation_status.unique()

# Analyze Species Conservation Status
conservation_counts = species.groupby('conservation_status').scientific_name.count().reset_index()

# print conservation_counts

# Analyze Species Conservation Status II
species.fillna('No Intervention', inplace = True)

conservation_counts_fixed = species.groupby('conservation_status').scientific_name.count().reset_index()

# Plotting Conservation Status by Species
protection_counts = species.groupby('conservation_status')    .scientific_name.count().reset_index()    .sort_values(by='scientific_name')
    
plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)),
       protection_counts.scientific_name.values)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
labels = [e.get_text() for e in ax.get_xticklabels()]
print ax.get_title()
# plt.show()



species['is_protected'] = species.conservation_status != 'No Intervention'

#sets up a Boolean – so it is either ‘True’ or ‘False’.

category_counts = species.groupby(['category', 'is_protected'])                         .scientific_name.count().reset_index()
  
#print category_counts.head()

category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()

#pivots the data 

category_pivot.columns = ['category', 'not_protected', 'protected']

#renames the columns 

category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

#new column with percent protected calculated.

print category_pivot.head()


#Mammals are NOT significantly different from amphibians, birds & fish but are from the rest.


contingency = [[30, 146],[75, 413]]
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(contingency)
print pval
pval_bird_mammal= 0.6875
pval_reptile_mammal = 0.03835
pval_vascular_plant_mammal = 1.44e-55



#contingency number are for the first pval (mammals versus birds)

import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('observations.csv')
#new csv being loaded 

species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep' in x)
# this line searches for the word ‘sheep’ in the column listed (common_name)

print(species.head(5))

species_is_sheep = species[species.is_sheep]
#this somehow returns only those things in the column where 
print species_is_sheep

sheep_species = species[(species.is_sheep) & (species.category == 'Mammal')]
#now we select all rows that have both a ‘true’ for sheep AND a category of mammal. 

print sheep_species


sheep_observations = observations.merge(sheep_species)
#this line merges the two dataframes observations & sheep_species
print sheep_observations.head()






obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
#grouping by park name and summing the number of observations.
print obs_by_park

plt.figure(figsize=(16, 4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)),
        obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observations of Sheep per Week')
plt.show()

