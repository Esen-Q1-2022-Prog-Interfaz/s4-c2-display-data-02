import pymysql.cursors
from Person import Person


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


def insertNewPerson(person):
    connection = createConnectionToDB()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `personinfodb`.`persondata`(`id`,`name`,`age`,`salary`) VALUES (%s,%s,%s,%s);"
            cursor.execute(sql, (person.id, person.name, person.age, person.salary))
        connection.commit()
