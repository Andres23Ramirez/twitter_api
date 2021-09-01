# Commented out IPython magic to ensure Python compatibility.
#import re
import nltk
import string
import csv
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from stop_words import get_stop_words
pd.set_option("display.max_colwidth",10)
warnings.filterwarnings("ignore",category=DeprecationWarning)
# %matplotlib inline
from textblob import TextBlob
import time
import string
from deep_translator import GoogleTranslator


#from google.colab import files
#files.upload()
##excel_file='tweets.csv'
##datos = pd.read_csv(excel_file,header=0)
def get_polarity(text):
  print('get polarity')
  #analysis=TextBlob(text)
  result = ''

  if text !='':
    #print(analysis.detect_language()=='es')
    #if analysis.detect_language()=='es':
    if True:
      #print(analysis.translate(from_lang='es',to='en'))
      #result = analysis.translate(from_lang='es',to='en')
      #print(result.sentiment.polarity)
      #result = analysis.translate(from_lang='es',to='en').sentiment.polarity
      #result = analysis.sentiment.polarity
      #time.sleep(5)
      translator = GoogleTranslator(source='auto', target='en').translate(text)
      #translation = translator.translate(text)
      #translation = translator.translate(text, src='es', dest=['es'])
      print('Text: ' + text)
      print('translator: ' + translator)
      analysis=TextBlob(translator)
      result = analysis.sentiment.polarity
  return result

def x_range(x):
  print(x)
  if x>0.2 :
    return 1
  elif x<0:
    return -1
  else:
    return 0

def get_result(test):
  #p_train = 0.99

  #train = datos[:int((len(datos))*p_train)] 
  #test = datos[int((len(datos))*p_train):]

  palabras_irrelevantes=get_stop_words('spanish')
  ##convert to lower case
  test['clean_text'] = test['full_text'].str.lower()
  ##Remove punctuations
  test['clean_text'] = test['clean_text'].str.replace('[^\w\s]',' ')
  ##Remove spaces in between words
  test['clean_text'] = test['clean_text'].str.replace(' +', ' ')
  print('Dentro modelo')
  ##Remove Numbers
  #test['clean_text'] = test['clean_text'].str.replace('\d+', '')
  ##Remove trailing spaces
  #test['clean_text'] = test['clean_text'].str.strip()
  ##Remove URLS
  #test['clean_text'] = test['clean_text'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])

  #stopwords = ["el", "para", "con", "contra", "de"]
  #texto = "el perro de ana se encontro con el de maria"
  #def eliminar_stopwords(test['clean_text'], stopwords):
  #    return ' '.join([word for word in texto.split(' ') if word not in stopwords])
  ##Remove stop words
  palabras_irrelevantes=get_stop_words('spanish')
  palabras_irrelevantes
  
  #stop = stopwords.words('english')
  palabras_irrelevantes.extend(["amp","https","co","Biden","rt"])
  test['clean_text'] = test['clean_text'].apply(lambda x: " ".join(x for x in x.split() if x not in palabras_irrelevantes ))
  print('2')
  ##Remove Text Column
  #del df_tweets['text']

  print('4')
  test['polarity']=test['clean_text'].apply(get_polarity)
  test['polarity'].head()
  print('Despues de polarity')

  test.head()

  test['result']=test['polarity'].apply(x_range)
  test.head(3)

  test['result'].value_counts()

  # Create our query
  myheaders = ['created_at', 'id', 'id_str','full_text', 'source','truncated','in_reply_to_status_id','in_reply_to_status_id_str','in_reply_to_user_id','in_reply_to_user_id_str','in_reply_to_screen_name','user','coordinates','place','quoted_status_id','quoted_status_id_str','is_quote_status','quoted_status','retweeted_status','quote_count','reply_count','retweet_count','favorite_count','entities','extended_entities','favorited','retweeted','possibly_sensitive','filter_level','lang','matching_rules', 'current_user_retweet', 'scopes', 'withheld_copyright', 'withheld_in_countries', 'withheld_scope', 'contributors', 'geo', 'metadata', 'display_text_range', 'clean_text', 'polarity', 'result']

  """ with open("results.csv", 'r+') as f:
    f.truncate(0)
    exist = False

  with open('results.csv', 'a', newline='') as myfile:    
    writer = csv.DictWriter(myfile, fieldnames=myheaders)
    if not exist:
      writer.writeheader()
      exist = True
    writer.writerows(test) 
    myfile.close() """

  return test

  
  """ labels='Neutro','Positivo', 'Negativo'
  colors=['blue','#167D7F','#98D7C2']
  plt.pie(test['result'].value_counts(),labels=labels,colors=colors,shadow=True,startangle=90,autopct='%1.1f%%')
  plt.title('Análisis de Sentimiento',fontsize=20)

  plt.axis('equal')
  plt.show()

  
  text =''.join(test.clean_text)
  text

  all_words=''.join([text for text in test['clean_text']]) 
  wordcloud=WordCloud(width=1024,height=800,random_state=21,max_font_size=100).generate(all_words)

  plt.figure(figsize=(16,12)) 
  plt.imshow(wordcloud,interpolation="bilinear")
  plt.axis('off')
  plt.show()



  fc = sns.factorplot(x="result", hue="result",
  data=test, kind="count")

  test_po=test[test['result']==1]
  test_po.head()

  all_wordsp=''.join([text for text in test_po['clean_text']]) 
  wordcloud=WordCloud(width=1024,height=800,random_state=21,max_font_size=100).generate(all_wordsp)

  plt.figure(figsize=(16,12)) 
  plt.imshow(wordcloud,interpolation="bilinear")
  plt.axis('off')
  plt.show()

  test_ne=test[test['result']==-1]
  test_ne.head()

  all_wordsn=''.join([text for text in test_ne['clean_text']]) 
  wordcloud=WordCloud(width=1024,height=800,random_state=21,max_font_size=100).generate(all_wordsn)

  plt.figure(figsize=(16,12)) 
  plt.imshow(wordcloud,interpolation="bilinear")
  plt.axis('off')
  plt.show()

  palabras_irrelevantes=get_stop_words('spanish')
  palabras_irrelevantes """

