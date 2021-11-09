#!/usr/bin/python3
""" script that takes in an argument """
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    user = argv[1]
    pwd = argv[2]
    dbname = argv[3]
    keyword = MySQLdb.escape_string(argv[4]).decode()
    query = "SELECT * FROM states WHERE name='" + keyword + "' ORDER BY id"
    db = MySQLdb.connect(host="localhost", user=user, passwd=pwd, db=dbname)
    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    db.close()
