import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',    
    password='Jjd7UU3m'
)

current = config.cursor()
# добавляем значения в таблицу 
id = 1
name = 'Yerassyl'
number = '87087309474'

sql = '''
    INSERT INTO phonebook VALUES (%s, %s, %s); 
'''

current.execute(sql, (id, name, number))

current.close()
config.commit()
config.close()