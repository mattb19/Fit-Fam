#Drop this file into backend to let it work
#Clear the fake data from the SQL data base using 'Delete from Posts'

from Database import db
from datetime import date
import random
import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()
poster = random.randint(1,7)
groupAssociation = 0

tagsList = ["Legs","Arms","Cardio","Core","Weights","Low Intensity","High Intensity"]

timeIncr = date.today()
for i in range(5):
    tagCombo = tagsList[random.randint(0,len(tagsList)-1)]
    for i in range(random.randint(0,3)):
        tagCombo = tagCombo + "," + tagsList[random.randint(0,len(tagsList)-1)]

    post = [timeIncr,random.randint(1,7),groupAssociation,"Lorem Ipsum, new",tagCombo,"",0]

    cursor.execute("INSERT INTO Posts (postDateTime, poster, groupAssociation, description, postTags, postImage, postLikes) VALUES (?,?,?,?,?,?,?)",(post))
    conn.commit()

cursor.close()
conn.close()