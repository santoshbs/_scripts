import pandas as pd
import numpy as np

print('reading dataframe...')
d = './' ##directory path of file
f = d + 'Users.csv'
df = pd.read_csv(f)
print('DONE reading dataframe with rows :: ' + str(df.shape[0]) + '!')

print('extracting emails...')
df = df.replace(np.nan, '')
df['email'] = df['AboutMe'].str.extract(r"([\w.-]+@[\w.-]+)").fillna('')
print('DONE extracting emails!')

print('creating dataframe of users with emails...')
df_email = df[df['email'].str.len() != 0]
print('DONE creating dataframe of users with emails :: ' + str(df_email.shape[0]) + ' users!')

print('cleaning email field...')
df_email['email'] = df['email'].str.rstrip('.')
print('DONE cleaning email field!')

print('saving users to csv...')
f_out = d + 'Users_with_email_v1.csv'
df_email.to_csv(f_out, index=False)
print('DONE saving users to csv!')

print('DONE with all!!')
