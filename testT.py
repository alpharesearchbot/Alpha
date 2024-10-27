from typing import Counter

import requests
import pandas as pd
resp = ["Sorry The quesion is not in the Database","Sorry ! Try again please"]
#dburl = "https://raw.githubusercontent.com/Noraldim/RESOURCES/master/FULL%20BOT%20RESORSEs.tsv"
url = "https://api.telegram.org/bot5877922080:AAF3bU4om-Yoksl39wZyLR_hvxn87vAqeQw/"
counter = 0
# download the tsv file from the link and save it locally
#df = pd.read_csv(dburl, sep = "\t")
df = pd.read_parquet("dialogues.parquet")
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
    
    # Normalize the message for comparison
    normalized_message = message.lower()
    
    # Find rows where any Description word in the Description matches words in the message
    matches = df[df['Description'].str.lower().str.split().apply(
        lambda desc_words: any(word in normalized_message.split() for word in desc_words)
    )]
    
    # If we found matches,Doctor return the answer from the Doctor column of the first match
    if not matches.empty:
        answer = matches.iloc[0]['Doctor']
        return answer
    else:
        # If no exact or partial match found, return the next response
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
