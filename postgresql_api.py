import psycopg2
import os
try:
    # db_secret = os.environ["DATABASE_URL"]
    db_secret = 'postgres://kotzvbazabjfis:02fadef119f22ae27bc1d654b0ac997077999514f8f582490eb9419cdb13abc2@ec2-52-200-48-116.compute-1.amazonaws.com:5432/dc5c7ci5mtp680'
    connection = psycopg2.connect(db_secret)
    connection.set_session(autocommit=True)

    cur = connection.cursor()
    cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    AND table_type='BASE TABLE';
    """)
    rows = cur.fetchall()
    print('Table list:')
    for row in rows:
        print("   ", row[0])
    cur.close()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

def get_student_data():
    cur = connection.cursor()
    cur.execute("""
    select first_name ,last_name , age
    from student;
    """)
    rows = cur.fetchall()
    print('student :')
    print(rows)
    cur.close()
    return rows

get_student_data()