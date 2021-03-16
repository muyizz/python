import cx_Oracle
conn = cx_Oracle.connect('yang/yang@127.0.0.1:1521/ORCL')
cursor = conn.cursor()
result = cursor.execute('select sysdate from dual')
print(result)