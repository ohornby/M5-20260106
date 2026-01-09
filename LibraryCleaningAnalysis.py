import pandas as pd

def fileLoader():
    data = pd.read_csv('03_LibrarySystembook.csv')
    return data

df = fileLoader()

blank_rows = df.isna().all(axis=1).sum()
dropped_rows = df.isna().any(axis=1).sum()
total_rows = len(df)
blank_row_pct = (blank_rows / total_rows) * 100

df = df.dropna()
df_clean = df.dropna()
df_clean['Id'] = df_clean['Id'].astype('int')
df_clean['Customer ID'] = df_clean['Customer ID'].astype('int')

df['Book checkout'] = pd.to_datetime(df['Book checkout'], dayfirst=True, errors='coerce')
df['Book Returned'] = pd.to_datetime(df['Book Returned'], dayfirst=True, errors='coerce')

incorrect_checkout_dates = df['Book checkout'].isna().sum()
incorrect_returned_dates = df['Book Returned'].isna().sum()
incorrect_date_formats = incorrect_checkout_dates + incorrect_returned_dates

df_clean['Book checkout'] = df_clean['Book checkout'].str.replace('"', '', regex=False)
df_clean['Book Returned'] = df_clean['Book Returned'].str.replace('"', '', regex=False)

df_clean['Book checkout'] = pd.to_datetime(df_clean['Book checkout'], dayfirst=True, errors='coerce')
df_clean['Book Returned'] = pd.to_datetime(df_clean['Book Returned'], dayfirst=True, errors='coerce')

df_clean = df_clean.dropna(subset=['Book checkout'])
df_clean = df_clean.dropna(subset=['Book Returned'])

df_clean['Days allowed to borrow'] = df_clean['Days allowed to borrow'].str.replace('2 weeks', '14', regex=False)
df_clean['Days allowed to borrow'] = df_clean['Days allowed to borrow'].astype('int')
df_clean['Books'] = df['Books'].str.title()

total_clean_rows = len(df_clean)
correct_checkout_dates = df_clean['Book checkout'].count()
correct_returned_dates = df_clean['Book Returned'].count()
correct_dates = correct_checkout_dates + correct_returned_dates

df_clean['Days checked out'] = (df_clean['Book checkout'] - df_clean['Book Returned']).dt.days
#df_clean['Overdue'] = 

print(df_clean)

print('..................Before Cleaning..................')
print(f'Total Raw Rows: {total_rows}')
print(f'Blank Rows: {blank_rows}')
print(f'% of Blank Rows: {blank_row_pct:.2f}%')
print(f'Dropped Rows: {dropped_rows}')
print(f'Incorrect Date Formats: {incorrect_date_formats}')
print('...................................................')
print('..................After Cleaning...................')
print(f'Total Rows: {total_clean_rows}')
print(f'Correct Date Formats: {correct_dates}')