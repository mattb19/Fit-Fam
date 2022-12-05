#Drop this file into backend to let it work
#Clear the fake data from the SQL data base using 'Delete from Posts'

from Database import db
from datetime import date,datetime
import random
import sqlite3

conn = sqlite3.connect('app.db')
cursor = conn.cursor()
poster = random.randint(1,7)
groupAssociation = 0

tagsList = ["Legs","Arms","Cardio","Core","Weights","Low Intensity","High Intensity"]

timeIncr = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
for i in range(15):
    tagCombo = tagsList[random.randint(0,len(tagsList)-1)]
    postTitle = "A Post by " + str(i)
    for i in range(random.randint(0,3)):
        tagCombo = tagCombo + "," + tagsList[random.randint(0,len(tagsList)-1)]

    post = [timeIncr,random.randint(1,7),groupAssociation,"Lorem Ipsum, Third Batch",tagCombo,"",0, postTitle]

    cursor.execute("INSERT INTO Posts (postDateTime, poster, groupAssociation, description, postTags, postImage, postLikes, postTitle) VALUES (?,?,?,?,?,?,?,?)",(post))
    conn.commit()

cursor.close()
conn.close()