import mysql.connector

urls = '(1,"https://i.ibb.co/VB0m5JK/1.webp"),(1,"https://i.ibb.co/JFrQf7k/2.webp"),(1,"https://i.ibb.co/M29Kfqs/image.webp"),(1,"https://i.ibb.co/tC7Wd8y/image.webp"),(1,"https://i.ibb.co/cxbdvf3/image.webp"),(1,"https://i.ibb.co/mThHxZk/image.webp"),(1,"https://i.ibb.co/dbXG0BM/image.webp"),(1,"https://i.ibb.co/YpVJ4ML/image.webp"),(1,"https://i.ibb.co/mvJrLRc/image.webp"),(1,"https://i.ibb.co/Y7s9P6J/image.webp"),(1,"https://i.ibb.co/Ybj31xn/image.webp"),(1,"https://i.ibb.co/X7TpchM/image.webp"),(1,"https://i.ibb.co/ccsRmfj/image.webp"),(1,"https://i.ibb.co/stb53nB/image.webp"),(1,"https://i.ibb.co/HrcsFZN/image.webp"),(1,"https://i.ibb.co/HrT4R6F/image.webp"),(1,"https://i.ibb.co/DMGhw6Q/image.webp"),(1,"https://i.ibb.co/CMjZStM/image.webp"),(1,"https://i.ibb.co/3r1wtdf/image.webp"),(1,"https://i.ibb.co/G7Dy2wP/image.webp"),(1,"https://i.ibb.co/tQSQ00X/image.webp"),(1,"https://i.ibb.co/Jjb110z/image.webp"),(1,"https://i.ibb.co/vDPv4Qz/image.webp"),(1,"https://i.ibb.co/5r3x1ww/image.webp"),(1,"https://i.ibb.co/pQKM9dJ/image.webp"),(1,"https://i.ibb.co/j8hVhfL/image.webp"),(1,"https://i.ibb.co/M61rQgg/image.webp"),(1,"https://i.ibb.co/mG29dLt/image.webp"),(1,"https://i.ibb.co/YcBm3J3/image.webp"),(1,"https://i.ibb.co/m9szHMw/image.webp")'

# specify the database connection details
host = 'sql12.freesqldatabase.com'
user = 'sql12599519'
password = 'sBsJNJa4bK'
database = 'sql12599519'

# create a connection to the database
cnx = mysql.connector.connect(host=host, user=user, password=password, database=database)

# check if the connection was successful
if cnx.is_connected():
    print('Connected to the database')

    cursor = cnx.cursor()
    # for url in urls:
    table_name = 'packs'
    column1_name = 'id'
    column2_name = 'packid'
    column3_name = 'url'
    # create_table_query = "INSERT INTO " + table_name + " ("+column2_name+","+ column3_name + ") VALUES " + urls + ""
    create_table_query = "UPDATE " + table_name + " SET iconurl = 'https://i.ibb.co/bdgHgYH/image.png'"
    print(create_table_query)
    cursor.execute(create_table_query)

    # commit the changes to the database
    cnx.commit()

    # close the cursor and database connection when done
    cursor.close()
    print("success")

else:
    print('Unable to connect to the database')

# close the database connection when done
cnx.close()
