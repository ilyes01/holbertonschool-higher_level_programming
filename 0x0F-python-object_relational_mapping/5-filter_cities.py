#!/usr/bin/python3
''' lists '''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id",
                (argv[4], ))
    row = cur.fetchall()
    i = 0
    for woof in row:
        if i != 0:
            print(", ", end="")
        print("%s" % woof, end="")
        i = i + 1
    print("")
    cur.close()
    db.close()
