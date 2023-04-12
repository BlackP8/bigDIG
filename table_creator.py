import psycopg2

conn = psycopg2.connect(host="localhost", database="greenplumdb", user="admin", password="qwerty", port='5432')
conn.autocommit = True
cur = conn.cursor()

commands = (
    """
    CREATE TABLE stg (
        date VARCHAR(50),
        id VARCHAR(20),
        points VARCHAR(100),
        temperature VARCHAR(6),
        hash VARCHAR(50)
    )
    """,
    """ CREATE TABLE dds (
        date VARCHAR(50),
        id VARCHAR(20),
        points VARCHAR(100),
        temperature VARCHAR(6),
        hash VARCHAR(50)
    )
    """)

for command in commands:
    cur.execute(command)

conn.commit()
cur.close()
conn.close()