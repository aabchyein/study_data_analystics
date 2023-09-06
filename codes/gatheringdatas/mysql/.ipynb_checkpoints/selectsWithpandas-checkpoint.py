# mysql connect package
# pip --> conda
import pymysql

# cnnect Mysql
# ip, port, username, password, database name
ip = 'localhost'  # 혹은 127.0.0.1 --> 192.168.0.31
port = '3306'   # port는 디폴트인 경우 안 써도 됨
username = 'root'
password = '!yojulab*'
database = 'db_cars'

# editor - statement
connect = pymysql.connect(host=ip, user=username, password=password, database=database)

# make select statement
sql_query = 'SELECT * FROM car_infors;'

# execute select query
import pandas
# return resultset and then display
df = pandas.read_sql(sql=sql_query, con=connect)

# close (창 닫기)
connect.close()

pass