from django.conf import settings
from django.db import connection


if connection.connection is None:
    cursor=connection.cursor()
    cursor.execute("select * from Users")
    user = cursor.fetchall()
    for row in user:
        print(row)