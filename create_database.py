import psycopg2
from urllib.parse import urlparse,uses_netloc


uses_netloc.append("postgres")

#USE THE LINK TO YOUR ELEPHANT SQL FOR BELOW
url=urlparse('postgres://erhjbmgq:JjwVb_0QxvpAOIMVUVDicYfDUHtZAmt6@stampy.db.elephantsql.com:5432/erhjbmgq')


conn=psycopg2.connect(database=url.path[1:],
	user=url.username,
	password=url.password,
	host=url.hostname,
	port=url.port
)
	#global conn

cur=conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS InputUserSentiment(id serial PRIMARY KEY, Name Varchar(50), Sentiment Varchar(500));')
conn.commit()

cur=conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS PictureSentimentValues(id serial PRIMARY KEY, HappyScore float, NeutralScore float, SurpriseScore float, SadScore float, FearScore float, DisgustScore float, AngryScore float);')
conn.commit()

