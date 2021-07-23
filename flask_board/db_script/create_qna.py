import sqlite3

'''
"no": 2,
"title": "제목이당",
"author": "홍길동",
"date": "2021-06-18",
"count": "124",
"status": "공개",
"attachment": "file-url"
'''

# flask_board/my.db
conn = sqlite3.connect('../my.db')
print("Opened db success")

conn.execute('CREATE TABLE QNA (title TEXT, author TEXT, date DATE, count INT, attachment TEXT)')
print("Create Table successs")
conn.close()