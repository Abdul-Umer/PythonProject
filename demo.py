import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="your_password"
)
mycursor = mydb.cursor()


class Task:
    def __init__(self,task,status):
        self.task=task
        self.status=status
    
    def __str__(self):
        return f'{self.task},{self.status}'
    
class TaskManager:
    def createDB():
        try:
            mycursor.execute("CREATE DATABASE TodoList")
            print("DataBase Created Succfully")
        except Exception:
            print('Issue while Creating DB')

    def useDB():
        try:
            mycursor.execute("use TodoList")
            print('using DB')
        except Exception:
            print('Already Using DB')
    def createTask():
        try:
            mycursor.execute("CREATE TABLE TaskMgr (name varchar(100),status varchar(20))")
            print('Created Table Successfully!')
        except Exception:
            print('Already Created Table')
    
    def insertTask():
        try:
            mycursor.execute("INSERT INTO TaskMgr(name,status) values('Coding','Pending')")
            mydb.commit()
            print('Inserted Successfully!')
        except Exception:
            print('Issue while Inserting')
    def updateTask():
        try:
            
            mycursor.execute("update TaskMgr set status='pending' where name='GYM'")
            mydb.commit()
            print('updated successfully')
        except Exception:
            print('Not updating..')
    
    def deleteTask():
        try:
            mycursor.execute("delete from TaskMgr  where name='Coding'")
            mydb.commit()
            print('Deleted Sucessfully!')
        except Exception:
            print('Not Deleted..')
    def readTask():
        try:
            mycursor.execute("SELECT name, status FROM TaskMgr")
            tasks = mycursor.fetchall()  # Fetch all the results from the query
            print("-------------Details--------------")
            for task in tasks:
                print("-------Name: %s, Status: %s-------" % (task[0], task[1]))  # Use proper formatting
        except Exception as e:
            print('Issue while reading data from DB:', e)


        
            
            


tm=TaskManager
tm.createDB()
tm.useDB()
#tm.createTask()
#tm.insertTask()
#tm.updateTask()
tm.deleteTask()     
tm.readTask()

#command to open mysql shell in VSCODE terminal
# mysql -u root -p 