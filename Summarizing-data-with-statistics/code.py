# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#path of the data file- path
data=pd.read_csv(path)
data['Gender'].replace('-','Agender')
gender_count=data['Gender'].value_counts()
gender_count.plot.barh()
#Code starts here 




# --------------
#Code starts here
alignment=data['Alignment'].value_counts()
labels = ['bad', 'good', 'natural']
plt.pie(alignment,labels=labels)
plt.title('Character alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson = sc_covariance/(sc_combat*sc_strength)
print("Pearson's Correlation Coefficient between Strength and Combat : ", sc_pearson)

#Subsetting the data with columns ['Intelligence', 'Combat']
ic_df = data[['Intelligence','Combat']].copy()
#Finding covariance between 'Intelligence' and 'Combat'
ic_covariance = ic_df.cov().iloc[0,1]
#Finding the standard deviation of 'Intelligence'
ic_intelligence = ic_df['Intelligence'].std()
#Finding the standard deviation of 'Combat'
ic_combat = ic_df['Combat'].std()
#Calculating the Pearson's correlation between 'Intelligence' and 'Combat'
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)
print("Pearson's Correlation Coefficient between Intelligence and Combat : ", ic_pearson)



# --------------
#Code starts here
 
total_high= data['Total'].quantile(q=0.99)

#Subsetting the dataframe based on 'total_high' 
super_best=data[data['Total']>total_high]

#Creating a list of 'Name' associated with the 'super_best' dataframe
super_best_names=list(super_best['Name'])

print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2,ax_3) = plt.subplots(1, 3, sharex=True, sharey=True)

ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(super_best['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set_title('Power')


