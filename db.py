import pymysql.cursors


def createConnectionToDB():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="personinfodb",
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )
    return connection


def selectAllPersonData():
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM personinfodb.persondata;"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
