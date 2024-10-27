from typing import Counter

import requests
import pandas as pd
resp = ["Sorry The quesion is not in the Database","Sorry ! Try again please"]

dburl = 'DataForTest.tsv'
url = "ourAPI :))"
counter = 0

df = pd.read_csv(dburl, sep = "\t")
#df = pd.read_parquet("dialogues.parquet")
def read(offset):

    para = {
            "offset" : offset
        }

    req = requests.get(url + "getUpdates", data = para)
    data = req.json()
    print(data)

    for result in data["result"]:
        send(result)

    if data["result"]:
        return data["result"][-1]["update_id"] + 1

def out(message):
  global counter

  normalized_message = message.lower()
  message_words = normalized_message.split()

  # Best fo Best it's read the sentence form the both side :) :) :)
  for i in range(len(message_words), 0, -1):
      sub_message = ' '.join(message_words[:i])
      matches = df[df['SORU '].str.lower().str.contains(sub_message)]

      if not matches.empty:
          answer = matches.iloc[0]['CEVAP']
          return answer

  # Retrun the ANSWER
  for word in message_words:
      matches = df[df['SORU '].str.lower().str.contains(word)]

      if not matches.empty:
          answer = matches.iloc[0]['CEVAP']
          return answer

  counter = (counter + 1) % len(resp)
  return resp[counter]


def send(result):

  text = result["message"]["text"]
  answer = out(text)


  parameter = {

      "chat_id" : result["message"]["chat"]["id"],
      "text" : answer  ,
      "reply_to_message_id" : None
  }


  req = requests.get(url + "sendMessage", data = parameter)
  print(req.text)

offset = 0

while True :
  offset = read(offset)