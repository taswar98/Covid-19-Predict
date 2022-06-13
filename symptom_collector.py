import csv
import pandas as pd

data = pd.read_csv("training.csv")
temp_list = []
dict_of_tweets = {}

for column_name in data.columns:
    temp_list = data[column_name].tolist()
    dict_of_tweets[column_name] = temp_list


##Converting all tweets to lowercase

num_tweets = len(data['Tweet'])

for x in range(0, num_tweets):
    data['Tweet'][x] = data['Tweet'][x].lower()

##Create a list of keywords/symptoms to search for
list_of_keywords = ['cough', 'covid', 'positive', 'sore throat', 'runny nose', 'fever', 'shortness of breathe']
keylist_size = len(list_of_keywords)

##Create a dictionary to store symptom string count pairs ex:("cough": 3, "fever": 10) 
symptom_count = {"cough" : 0, "covid" : 0, "positive" : 0, "sore throat" : 0, "runny nose" : 0, "fever": 0, "shortness of breathe" :0}

count_list= []
counter = 0
symptom_count

##Check to see if each tweet contains the symptom keywords
for tweets in data['Tweet']:
    for symptoms in list_of_keywords:
        if symptoms in tweets:
            symptom_count[symptoms] += 1
            counter+=1    

count_list.append(symptom_count)

#Write back the symptom counts into a csv file
with open('counts.csv', 'w') as csvfile:
    ##writer = csv.DictWriter(csvfile, fieldnames = list_of_keywords)
    writer = csv.DictWriter(csvfile, fieldnames = list_of_keywords)
    writer.writeheader()
    writer.writerows(count_list)