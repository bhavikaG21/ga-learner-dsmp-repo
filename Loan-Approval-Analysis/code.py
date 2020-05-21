# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include='object')
print('Categorical val : ',categorical_var)

numerical_var = bank.select_dtypes(include='number')
print('Numeriacl value : ', numerical_var)
# code ends here


# --------------
# code starts here
banks = bank.drop('Loan_ID',axis=1)
print(banks.isnull().sum())

bank_mode = banks.mode()
banks = banks.fillna('NaN')
banks
#code ends here


# --------------
# Code starts here




avg_loan_amount = pd.pivot_table(banks,values='LoanAmount',index =['Gender', 'Married', 'Self_Employed'], aggfunc = np.mean)

print('Avg loan amt : ',avg_loan_amount)



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].shape[0]

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].shape[0]

percentage_se = (loan_approved_se/banks['Loan_Status'].count())*100
print('percentage of loan approval for self employed people: \n',percentage_se)

percentage_nse = (loan_approved_nse/banks['Loan_Status'].count())*100
print('percentage of loan approval for people who are not self-employed: \n',percentage_nse)






# code ends here


# --------------
# code starts here





loan_term=banks['Loan_Amount_Term'].apply(lambda x : int(x) / 12)
#loan_term = banks[banks.apply(lambda x : x['Loan_Amount_Term']/12,axis=1)]
big_loan_term = ((loan_term>=25))
#banks['loan_term']
big_loan_term=554

# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]

mean_values = loan_groupby.mean()
mean_values
# code ends here


