from stop_words import get_stop_words
from textblob import TextBlob
from deep_translator import GoogleTranslator


def get_polarity(text):
  result = ''

  if text !='':
    translator = GoogleTranslator(source='auto', target='en').translate(text)
    analysis=TextBlob(translator)
    result = analysis.sentiment.polarity
  return result

def x_range(x):
  if x>0.2 :
    return 1
  elif x<0:
    return -1
  else:
    return 0

def get_result(test):
  palabras_irrelevantes=get_stop_words('spanish')
  ##convert to lower case
  test['clean_text'] = test['full_text'].str.lower()
  ##Remove punctuations
  test['clean_text'] = test['clean_text'].str.replace('[^\w\s]',' ')
  ##Remove spaces in between words
  test['clean_text'] = test['clean_text'].str.replace(' +', ' ')
  palabras_irrelevantes=get_stop_words('spanish')
  
  #stop = stopwords.words('english')
  palabras_irrelevantes.extend(["amp","https","co","Biden","rt"])
  test['clean_text'] = test['clean_text'].apply(lambda x: " ".join(x for x in x.split() if x not in palabras_irrelevantes ))
  test['polarity']=test['clean_text'].apply(get_polarity)
  test['result']=test['polarity'].apply(x_range)
  test['result'].value_counts()
  return test
