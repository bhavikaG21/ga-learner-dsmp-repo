# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path,delimiter=",",skip_header = 1)

print("Data: \n\n",data)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

census=np.concatenate((data,new_record))
print(census)
#Code starts here



# --------------
#Code starts here
age = census[:,0]
print("Age array: ",age)
print("="*50)

max_age = max(age)
print("Max age:", max_age)
print("="*50)

min_age = min(age)
print("Min age:", min_age)
print("="*50)

age_mean = np.mean(age)
print("Mean: ", age_mean)
print("="*50)

age_std = np.std(age)
print("SD: ", age_std)


# --------------
#Code starts here

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print(np.array([len_0, len_1, len_2,len_3,len_4]))

minority_race = np.argmin(np.array([len_0, len_1, len_2,len_3,len_4]))

print("Min no. of citizens: ", minority_race)


# --------------
#Code starts here

senior_citizens= census[census[:,0]>60]

working_hours_sum = np.sum(senior_citizens[:,6])
print('Addion of working hours : ',working_hours_sum)#1917

senior_citizens_len = len(senior_citizens)
print('Length of Senior citizens', senior_citizens_len)

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)#31.42



# --------------
#Code starts here
#high = [i for i in np.array(census[:,1]) if i > 10]
#low = [i for i in np.array(census[:,1]) if i <= 10]

high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)

compare = avg_pay_high-avg_pay_low
print(compare)


