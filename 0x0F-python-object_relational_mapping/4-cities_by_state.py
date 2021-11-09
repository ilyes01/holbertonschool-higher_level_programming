#!/usr/bin/python3
""" script that lists all cities """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    db = MySQLdb.connect(host="localhost", user=user, passwd=pwd, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM states INNER JOIN cities ON\
            states.id = cities.state_id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
