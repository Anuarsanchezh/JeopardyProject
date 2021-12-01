import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')
#print(jeopardy.head())
#print('Before:', jeopardy.columns)

#Cleaning the DataFrame. Some column names have innecesary spaces
jeopardy.rename(columns={
  'Show Number': 'Show',
  ' Air Date': 'Date',
  ' Round': 'Round',
  ' Category': 'Cat',
  ' Value': 'Val',
  ' Question': 'Q',
  ' Answer': 'A'},
  inplace=True)
#print('After:', jeopardy.columns)

#def filters(list):
#  jeopardy['Filtering'] = jeopardy.Q.apply(lambda x: any(element in x for element in list))
#print(jeopardy.iloc[1,:])

#The following function filters the dataset for questions that contains all of the words in a list of words. For example, when the list ["King", "England"] was passed to our function, the function returned a DataFrame where every row had the strings "King" and "England" somewhere in its "Question".
def filters(list):
  lower_list = [elem.lower() for elem in list]
  new_df = jeopardy[jeopardy.Q.apply(lambda x: any(element in x.lower() for element in lower_list))]
  return new_df

#print(filters(["Pe"]))
#print(filters(['No. 2:  1912 Olympian; football star at Carlisle Indian School; 6 MLB seasons with the Reds, Giants & Braves']))


jeopardy['Val_float'] = jeopardy.Val.apply(lambda x: x if x == 'None' else float(x.replace(',', '').replace('$', '')))
#print(jeopardy.Val_float)

#print(filters(['King']).Val_float.reset_index().mean())

def count_unique_answers(word_string):
  print(filters([word_string]).A.value_counts())

#count_unique_answers("King")

print(filters(['Computer'])[(filters(['Computer']).Date > '1990-01-01') & (filters(['Computer']).Date < '2000-01-01')])

print(filters(['Computer'])[(filters(['Computer']).Date > '2000-01-01')])
print(filters(['Computer']))
