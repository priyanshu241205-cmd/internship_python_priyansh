import sqlite3

conn = sqlite3.connect("mydatabase.db")
#sql = '''
#insert into emp (name,mob, city)
#values("abc","1234567890","delhi")
##'''
#conn.execute(sql)
#conn.commit()
#conn.close()
#print("Data inserted successfully")
#sql= "select * from Emp"
#res=conn.execute(sql)
#for row in res:
  #  print(row)
    
    #delete data
#import sqlite3

#conn = sqlite3.connect("mydatabase.db")

#sql = '''
#delete from emp
#where name = "abc"
#'''

#conn.execute(sql)
#conn.commit()

#print("Data deleted successfully")

#conn.close()




# order by 
#import sqlite3

#conn = sqlite3.connect("mydatabase.db")

#ql = "select * from emp order by name"

#res = conn.execute(sql)

# row in res:
 #   print(row)

#conn.close()


#delete by id
#import sqlite3

#conn = sqlite3.connect("mydatabase.db")

#sql = '''
#delete from emp
#where id = 1
#'''

#conn.execute(sql)
#conn.commit()

#print("Record deleted successfully")

#conn.close()




#update data


conn = sqlite3.connect("mydatabase.db")

sql = '''
update emp
set mob = "0987654321"
where name = "John Doe"
'''

conn.execute(sql)
conn.commit()

print("Data updated successfully")

conn.close()
