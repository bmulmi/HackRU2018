import paralleldots

paralleldots.set_api_key("PBgqFCR9T70FVQh7AJ688gugecn5doufgAiSmz3137A")

print(paralleldots.get_api_key())
#path= "/try.jpg"
path="D:\HackRU/try.jpg"

print( "\nFacial Emotion" )
values= paralleldots.facial_emotion(path)
print(values)

import json
from pprint import pprint

#values[""]
#print(values['facial_emotion'][0]['tag']) #OUTPUTS HAPPY. WORKING

significantemotions_andvalues={}

emotions=[]
#Happy, Neutral, Surprise, Sad, Fear, Disgust, Angry

if (values['facial_emotion'][0]['tag']) == 'Happy':
    happinessscore = values['facial_emotion'][0]['score']
    emotions.append(happinessscore)

if (values['facial_emotion'][1]['tag']) == 'Neutral':
    neutralcore = values['facial_emotion'][1]['score']
    emotions.append(neutralcore)

if (values['facial_emotion'][2]['tag']) == 'Surprise':
    surprisescore = values['facial_emotion'][2]['score']
    emotions.append(surprisescore)

if (values['facial_emotion'][3]['tag']) == 'Sad':
    sadscore = values['facial_emotion'][3]['score']
    emotions.append(sadscore)

if (values['facial_emotion'][4]['tag']) == 'Fear':
    fearscore = values['facial_emotion'][4]['score']
    emotions.append(fearscore)

if (values['facial_emotion'][5]['tag']) == 'Disgust':
    disgustscore = values['facial_emotion'][5]['score']
    emotions.append(disgustscore)

if (values['facial_emotion'][6]['tag']) == 'Angry':
    angryscore=values['facial_emotion'][6]['score']
    emotions.append(angryscore)
print()
print('The emotion scores in order are:')
for one in emotions:
    print(one)


import psycopg2
from urllib.parse import urlparse,uses_netloc


uses_netloc.append("postgres")

#USE THE LINK TO YOUR ELEPHANT SQL FOR BELOW
url=urlparse('postgres://erhjbmgq:JjwVb_0QxvpAOIMVUVDicYfDUHtZAmt6@stampy.db.elephantsql.com:5432/erhjbmgq')

#postgres://erhjbmgq:JjwVb_0QxvpAOIMVUVDicYfDUHtZAmt6@stampy.db.elephantsql.com:5432/erhjbmgq
conn=psycopg2.connect(database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)


cur=conn.cursor()
print("----------------------------")
print(happinessscore)
cur.execute('INSERT INTO PictureSentimentValues (HappyScore, NeutralScore, SurpriseScore, SadScore, FearScore, DisgustScore, AngryScore) VALUES (%s,%s,%s,%s,%s,%s,%s)',(happinessscore, neutralcore,surprisescore,sadscore,fearscore,disgustscore,angryscore))
conn.commit()