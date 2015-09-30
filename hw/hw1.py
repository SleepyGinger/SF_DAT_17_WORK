'''
Move this code into your OWN SF_DAT_15_WORK repo

Please complete each question using 100% python code

If you have any questions, ask a peer or one of the instructors!

When you are done, add, commit, and push up to your repo

This is due 7/1/2015
'''


import pandas as pd
# pd.set_option('max_colwidth', 50)
# set this if you need to

killings = pd.read_csv('hw/data/police-killings.csv')
killings.head()

# 1. Make the following changed to column names:
# lawenforcementagency -> agency
# raceethnicity        -> race
killings.rename(columns={'lawenforcementagency':'agency', 'raceethnicity':'race'}, inplace=True)

# 2. Show the count of missing values in each column
killings.isnull().sum()

# 3. replace each null value in the dataframe with the string "Unknown"
killings=killings.fillna(value='Unknown')

# 4. How many killings were there so far in 2015?
killings[killings.year == 2015].info()

# 5. Of all killings, how many were male and how many female?
killings.gender.value_counts()

# 6. How many killings were of unarmed people?
killings.armed.value_counts()

# 7. What percentage of all killings were unarmed?
len(killings.armed=='No')/float(len(killings))

# 8. What are the 5 states with the most killings?
killings.state.value_counts()

# 9. Show a value counts of deaths for each race
killings.race.value_counts()

# 10. Display a histogram of ages of all killings
killings.age.hist()

# 11. Show 6 histograms of ages by race
killings.age.hist(by=killings.race, sharex=True, sharey=True)

# 12. What is the average age of death by race?
killings.groupby('race').age.mean()

# 13. Show a bar chart with counts of deaths every month
killings.month.value_counts().plot(kind='bar')
plt.show()


###################
### Less Morbid ###
###################

majors = pd.read_csv('hw/data/college-majors.csv')
majors.head()

# 1. Delete the columns (employed_full_time_year_round, major_code)
majors.drop(['Employed_full_time_year_round', 'Major_code'], axis=1, inplace=True)

# 2. Show the cout of missing values in each column
majors.isnull().sum()

# 3. What are the top 10 highest paying majors?
majors.sort_index(by='median', ascending=False).head(10)

# 4. Plot the data from the last question in a bar chart, include proper title, and labels!
majors.sort_index(by='median', ascending=False).head(10).plot(x='major', y='median', kind='bar', title='supa title')

# 5. What is the average median salary for each major category?
majors.groupby('major_category')[['median']].mean()

# 6. Show only the top 5 paying major categories
majors.groupby('major_category')[['median']].mean().sort_index(by='median', ascending=False).head(5)

# 7. Plot a histogram of the distribution of median salaries
majors.mmedian.hist()

# 8. Plot a histogram of the distribution of median salaries by major category


# 9. What are the top 10 most UNemployed majors?
# What are the unemployment rates?

# 10. What are the top 10 most UNemployed majors CATEGORIES? Use the mean for each category
# What are the unemployment rates?

# 11. the total and employed column refer to the people that were surveyed.
# Create a new column showing the emlpoyment rate of the people surveyed for each major
# call it "sample_employment_rate"
# Example the first row has total: 128148 and employed: 90245. it's 
# sample_employment_rate should be 90245.0 / 128148.0 = .7042

# 12. Create a "sample_unemployment_rate" colun
# this column should be 1 - "sample_employment_rate"
