# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:04:58 2018
@author: souravg

"""
"""
Read the dataset from the below link
https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv

Questions:
1. Delete unnamed columns
2. Show the distribution of male and female
3. Show the top 5 most preferred names
4. What is the median name occurence in the dataset
5. Distribution of male and female born count by states
"""
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
print("Before deleting unnamed columns")
print('-'*31, sep='')
print(df.head())
print("\nAfter deleting unnamed columns")
print('-'*30, sep='')
del df['Unnamed: 0']  # Delete unnamed columns
print(df.head())
print("\nDistribution of Male and Female")
print('-'*31, sep='')
print("Total number of Males are %d"%len(df[df.Gender=='M']))
print("Total number of Females are %d"%len(df[df.Gender=='F']))
print('-'*31, sep='')
print("\nTop 5 most preferred names")
print('-'*27, sep='')
result =df.groupby(['Name'])["Count"].sum() # Grouping on the basis of Name and adding their count occurences
Top5 = result.reset_index().sort_values('Count',ascending=False).set_index('Count').head(5) # Show the top 5 most preferred names
for lab, row in Top5.iterrows() :
    print(row['Name'] + " has occurance of " + str(lab) + " times")
    
Median = result.median()
print("\nMedian is %f" %Median)
print("Median name occurence in the dataset are as follows :-")
print('-'*55, sep='')
print(result[result==int(Median)]) # Median name occurence in the dataset

dist_gender_state_result =df.groupby(['Gender','State'])["Count"].count() # Grouping of male and female born count by states
#print(dist_gender_state_result)
print('-'*55, sep='')
print("Total Number of Females in Alaska are %d"%dist_gender_state_result['F']['AK'])
print("Total Number of Females in Alabama are %d"%dist_gender_state_result['F']['AL'])
print("Total Number of Males in Alaska are %d"%dist_gender_state_result['M']['AK'])
print("Total Number of Males in Alabama are %d"%dist_gender_state_result['M']['AL'])
print('-'*55, sep='')