import os
import re
import sqlite3

conn = sqlite3.connect('reddit.db')

#conn.execute("DROP TABLE data")

conn.execute('''CREATE TABLE data
         (Id TEXT PRIMARY KEY     NOT NULL,
         Mentions           INT    NOT NULL);''')


directory = os.fsencode("data")
    
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    match = re.findall('\d+', filename)
    separator = '-'
    if (len(match[2]) == 1):
        match[2] = "0" + match[2]
    date = separator.join(match)

    with open("data/" + filename) as file2:  # read coin file
        for line in file2:
            info = line.rstrip('\n').split(": ")
            try:
                conn.execute('INSERT INTO data (Id, Mentions) VALUES ("' + date + '-' + info[0] + '", '+ info[1] + ')')
            except:
                pass

    conn.commit()
    print(date)
