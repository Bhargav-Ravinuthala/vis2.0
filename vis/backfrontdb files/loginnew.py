import sqlite3
import csv

DB = "sqlite.db"


# connect to our database and insert a new user
def insert_user(user_name, user_password, db=DB):
    """Insert user name and user password into DB
    :param user:
    :param password:
    :param db:
    :return: Ok msg if user inserted, Error msg if not
    """
    
    # connect to the database
    db_connection = None
    
    # try the query and commit
    try:
        db_connection = sqlite3.connect(db)
        cursor = db_connection.cursor()
     
        print("[*] DB Connection Successful!")
        
        #sql = '''INSERT INTO users.user_name,exam_metadata.exam_url,exam_metadata.video1,exam_metadata.video2,exam_metadata.video3 from users left join on users.id = exam_metadata.user_id and where users.id = 2 
              #VALUES(?,?,?,?,?,??,?,?)'''

        sql ='''insert user_name,password, role VALUES  (?, ?, ?) into users'''
        
        
        cursor.execute(sql, (user_name, user_password, 'Admin'))
        db_connection.commit()
        print("[*] User Inserted!")
        user_id_sql= '''select ID from users where user_name = ? and password = ?  '''
        
        cursor.execute (user_id_sql, (user_name, user_password)
        
        

        
        db_connection.close()
        print("newly inserted User_id :" + id_fetch )
        return "[*] User Inserted!"
    
    except ConnectionError as e:
        print(f"[!] DB connection aborted! Error:{e}")
        return f"[!] DB connection aborted! Error:{e}"
    
    except sqlite3.Error as e:
        print(f"[!] SQL error! Error:{e}")
        return f"[!] SQL error! Error:{e}"

# connect to our database and retrieve all usernames    
def retrieve_username(db=DB):
    """Retrieve usernames from the users table
    :param db:
    :return: username
    """
    db_connection = None
    
    try:
        db_connection = sqlite3.connect(db)
        cursor = db_connection.cursor()
        
        print("[*] DB Connection Successful!")
        
        sql = '''select users.user_name,exam_metadata.exam_url,exam_metadata.video1,exam_metadata.video2,exam_metadata.video3 from users left join on users.id = exam_metadata.user_id and where users.id = ? '''
            
        cursor.execute(sql,(id_fetch))
        users = cursor.fetchall()
        db_connection.commit()
        print("[*] Users Retrieved!")
        db_connection.close()
        
        print(users)
        return users
    
    except Exception as e:
        print(f"[!] DB connection aborted! Error:{e}")
        return f"[!] DB connection aborted! Error:{e}"

# connect to our database and retrieve all userdata    
def retrieve_users(db=DB):
    """Retrieve all users from the users table
    :param db:
    :return: users
    """
    db_connection = None
    
    try:
        db_connection = sqlite3.connect(db)
        cursor = db_connection.cursor()
        
        print("[*] DB Connection Successful!")
        
        sql = '''SELECT rowid, username, password FROM users'''
            
        cursor.execute(sql)
        users = cursor.fetchall()
        db_connection.commit()
        print("[*] Users Retrieved!")
        db_connection.close()
        
        print(users)
        return users
    
    except Exception as e:
        print(f"[!] DB connection aborted! Error:{e}")
        return f"[!] DB connection aborted! Error:{e}"

DB2 = "front2.db"
def video(db = DB2):
    db_connection = None
    try:
        
        db_connection = sqlite3.connect(db)
        cursor = db_connection.cursor()
        
        print("[*] DB Connection Successful!")
        
        sql = '''SELECT ID, v1, v2, v3 FROM front where ID =2'''
            
        cursor.execute(sql)
        users = cursor.fetchall()
        db_connection.commit()
        print("[*] Users Retrieved!")
        db_connection.close()
        
        print(users)
        fp = open('quired_data.csv', 'w')
        myFile = csv.writer(fp)
        myFile.writerows(users)
        fp.close()
        return users
    except Exception as e:
        print(f"[!] DB connection aborted! Error:{e}")
        return f"[!] DB connection aborted! Error:{e}"
        

    
    


if __name__ == '__main__':
    # insert_user("dummy_user", "admin")
    retrieve_users()
    retrieve_username()
    video()
    
