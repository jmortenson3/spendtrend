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

    #print(type(df['Memo']))  # Series
    df['Fixed_Desc'] = fixed_desc
    df['Memo'] = df['Memo'].astype(str)
    df['Desc'] = df.Fixed_Desc + ' ' + df.Memo

    df.to_csv('./data/test_output.csv')
    col_category = []
    for row in df.Desc:
        if row in 'Deposit nan':
            col_category.append('Deposit')
        elif any(x in row for x in category.class_instance.GARBAGE):
            col_category.append('Garbage')
        elif any(x in row for x in category.class_instance.STUDENT_LOANS):
            col_category.append('Student Loans')
        elif any(x in row for x in category.class_instance.TRANSPORTATION):
            col_category.append('Transportation')
        elif any(x in row for x in category.class_instance.EDUCATION):
            col_category.append('Education')
        elif any(x in row for x in category.class_instance.HOTELS):
            col_category.append('Hotels')
        elif any(x in row for x in category.class_instance.ATM):
            col_category.append('ATMs')
        elif any(x in row for x in category.class_instance.SUBSCRIPTIONS):
            col_category.append('Subscriptions')
        elif any(x in row for x in category.class_instance.ENTERTAINMENT):
            col_category.append('Entertainment')
        elif any(x in row for x in category.class_instance.SHOPPING):
            col_category.append('Shopping')
        elif any(x in row for x in category.class_instance.GAS_STATIONS):
            col_category.append('Gas Station')
        elif any(x in row for x in category.class_instance.PHONE):
            col_category.append('Phone')
        elif any(x in row for x in category.class_instance.LUNCHES):
            col_category.append('Lunches')
        elif any(x in row for x in category.class_instance.PAY_CHECKS):
            col_category.append('Pay Check')
        elif any(x in row for x in category.class_instance.PET_SUPPLIES):
            col_category.append('Pet Supplies')
        elif any(x in row for x in category.class_instance.MORTGAGES):
            col_category.append('Mortgage')
        elif any(x in row for x in category.class_instance.ENERGY):
            col_category.append('Energy')
        elif any(x in row for x in category.class_instance.CREDIT_CARDS):
            col_category.append('Credit Card')
        elif any(x in row for x in category.class_instance.CAR_PAYMENTS):
            col_category.append('Car Payments')
        elif any(x in row for x in category.class_instance.UTILITIES):
            col_category.append('Utilities')
        elif any(x in row for x in category.class_instance.RESTAURANTS):
            col_category.append('Restaurants')
        elif any(x in row for x in category.class_instance.AUTO_INSURANCE):
            col_category.append('Auto Insurance')
        elif any(x in row for x in category.class_instance.GROCERIES):
            col_category.append('Groceries')
        elif any(x in row for x in category.class_instance.HAIR_CUTS):
            col_category.append('Hair Cuts')
        elif any(x in row for x in category.class_instance.INTERNET):
            col_category.append('Internet')
        elif any(x in row for x in category.class_instance.TRANSFERS):
            col_category.append('Transfers')
        elif any(x in row for x in category.class_instance.HOMEOWNERS_INSURANCE):
            col_category.append('Homeowner\'s Insurance')
        elif any(x in row for x in category.class_instance.TAXES):
            col_category.append('Taxes')
        else:
            col_category.append('uncategorized')
    
    df['Category'] = col_category
    df['Amount Credit'].fillna(0, inplace=True)
    df['Amount Debit'].fillna(0, inplace=True)
    #df['Amount'] = df['Amount Credit'] if df['Amount Debit'].empty else df['Amount Credit']
    df['Amount'] = df['Amount Credit'] + df['Amount Debit']
    print(df.groupby(['Category'])[['Amount']].apply(lambda x: np.sum(x)))
    #print(df[['Amount']].apply(lambda x: np.mean(x)))
    

if __name__ == '__main__':
    main()