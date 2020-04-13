# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Code starts here
data=np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
census = np.concatenate((data, new_record), axis=0)
print(census)


# --------------
#Code starts here
age = census[...,0]
print(age)
max_age = age.max()
min_age = age.min()
age_mean = age.mean()
age_std = np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


# --------------
#Code starts here
#races = census[...,2]
#print(races)
race_0 = census[census[...,2]==0]
len_0 = np.shape(race_0)[0]
print(len_0)
race_1 = census[census[...,2]==1]
len_1 = np.shape(race_1)[0]

race_2 = census[census[...,2]==2]
len_2 = np.shape(race_2)[0]

race_3 = census[census[...,2]==3]
len_3 = np.shape(race_3)[0]
race_4 = census[census[...,2]==4]
len_4 = np.shape(race_4)[0]

lengths = np.array([len_0, len_1, len_2, len_3, len_4])
min_race_len = lengths.min()

def minority():
    if min_race_len == len_0:
        return 0
    if min_race_len == len_1:
        return 1
    if min_race_len == len_2:
        return 2
    if min_race_len == len_3:
        return 3
    if min_race_len == len_4:
        return 4

minority_race = minority()
print(minority())



# --------------
#Code starts here
senior_citizens = census[census[...,0]>60]
working_hours_sum = senior_citizens[...,6].sum()
print(working_hours_sum)
senior_citizens_len = np.shape(senior_citizens)[0]
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[...,1]>10]
low = census[census[...,1]<=10]
avg_pay_high=high[...,7].mean()
avg_pay_low = low[...,7].mean()
print(avg_pay_high)
print(avg_pay_low)


