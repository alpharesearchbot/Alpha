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