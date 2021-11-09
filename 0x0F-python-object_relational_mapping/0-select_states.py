#!/usr/bin/python3
"""
Lists all states
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    lists = cursor.fetchall()
    for row in lists:
        print(row)
    cursor.close()
    db.close()
