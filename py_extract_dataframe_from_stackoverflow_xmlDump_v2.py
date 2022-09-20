'''
Script to extract Stack Overflow Users.xml dup (https://archive.org/download/stackexchange_20220307) into a CSV
'''
import pandas as pd
import xml.etree.ElementTree as ET

d = './' ##directory path for xml
f = d + 'Users.xml' ##file name

print('reading and parsing xml file')
xml = ET.parse(f)
root = xml.getroot()
print('DONE reading and parsing xml file!')

print('creating a list of dicts')
list_dicts = []
for row in root:
    print(row.attrib['Id'])
    list_dicts.append(row.attrib)
print('DONE creating a list of dicts:: ' + str(len(list_dicts)) + '!')

print('converting to dataframe')
df = pd.DataFrame.from_dict(list_dicts)
print('DONE converting to dataframe!')

print('saving dataframe to file')
df.to_csv(d + 'Users.csv')
print('DONE saving dataframe to file!')

print('Done with all!!')