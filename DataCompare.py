import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')

print(dsn)

conn = cx_Oracle.connect("hr", "hr", dsn)
curs = conn.cursor()

curs.execute("select table_name,column_name from ALL_tab_columns where OWNER='userid' order by table_name")
