import json
from json.tool import main
import pandas as pd
from sqlalchemy import desc

#with open("farmers-protest-tweets-2021-03-5.json","r") as file:
    #data = json.load(file)
    #for tweetcount in data['retweetCount']:
        #print('First name:', client['first_name'])
    #print(data)

def main():
    tmp = []
    for line in open('farmers-protest-tweets-2021-2-4.json','r'):
        tmp.append(json.loads(line))

    df = pd.DataFrame(tmp)
    print(df.columns)
    opcion = int(input("seleccione la funcion que desea ver: "))
    if opcion == 1:
        retweet10(df)
    if opcion == 2:
        users(df)


def retweet10(df):
    d1 = df.sort_values(by='retweetCount', ascending=False)
    print(d1.head(10))

def users(df):
    d1 = df.user
    d2 = []
    for data in d1:
        d2.append(data['username'])
    df2 = pd.DataFrame(d2)
    df2 = df2.value_counts(ascending=False)
    print(df2.head(10))

main()



