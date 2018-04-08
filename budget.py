import pandas as pd
import numpy as np
import category
import sys
#import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('./data/Export.csv', parse_dates=['Date'], 
        index_col=['Date'], usecols=['Date', 'Description', 'Memo', 'Amount Debit', 'Amount Credit'])
    excludeWords = ['Check', 'Card', 'Withdrawal', 'External',
                    'to', 'Internet', '*', '-']
    fixed_desc =[]
    for row in df.Description:
        fixed_desc.append(' '.join(i for i in row.split() if i not in excludeWords))

    df['Fixed_Desc'] = fixed_desc
    df['Memo'] = df['Memo'].astype(str)
    df['Desc'] = df.Fixed_Desc + df.Memo

    df.to_csv('./data/test_output.csv')
    col_category = []
    for row in df.Desc:
        if row in 'Depositnan':
            col_category.append('Deposit')
        elif any(x in row for x in category.class_instance.GARBAGE):
        #elif row in category.class_instance.GARBAGE:
            col_category.append('Garbage')
        elif row in category.class_instance.STUDENT_LOANS:
            col_category.append('Student Loans')
        elif row in category.class_instance.TRANSPORTATION:
            col_category.append('Transportation')
        elif row in category.class_instance.EDUCATION:
            col_category.append('Education')
        elif row in category.class_instance.HOTELS:
            col_category.append('Hotels')
        elif row in category.class_instance.ATM:
            col_category.append('ATMs')
        elif row in category.class_instance.SUBSCRIPTIONS:
            col_category.append('Subscriptions')
        elif row in category.class_instance.ENTERTAINMENT:
            col_category.append('Entertainment')
        elif row in category.class_instance.SHOPPING:
            col_category.append('Shopping')
        elif row in category.class_instance.GAS_STATIONS:
            col_category.append('Gas Station')
        elif row in category.class_instance.PHONE:
            col_category.append('Phone')
        elif row in category.class_instance.LUNCHES:
            col_category.append('Lunches')
        elif row in category.class_instance.PAY_CHECKS:
            col_category.append('Pay Check')
        elif row in category.class_instance.PET_SUPPLIES:
            col_category.append('Pet Supplies')
        elif row in category.class_instance.MORTGAGES:
            col_category.append('Mortgage')
        elif row in category.class_instance.ENERGY:
            col_category.append('Energy')
        elif row in category.class_instance.CREDIT_CARDS:
            col_category.append('Credit Card')
        elif row in category.class_instance.CAR_PAYMENTS:
            col_category.append('Car Payments')
        elif row in category.class_instance.UTILITIES:
            col_category.append('Utilities')
        elif row in category.class_instance.RESTAURANTS:
            col_category.append('Restaurants')
        elif row in category.class_instance.AUTO_INSURANCE:
            col_category.append('Auto Insurance')
        elif row in category.class_instance.GROCERIES:
            col_category.append('Groceries')
        elif row in category.class_instance.HAIR_CUTS:
            col_category.append('Hair Cuts')
        elif row in category.class_instance.INTERNET:
            col_category.append('Internet')
        else:
            col_category.append('uncategorized')
    
    df['Category'] = col_category

    df.to_csv('./data/output.csv', columns=['Desc', 'Category'])



if __name__ == '__main__':
    main()