import sys
 
def SelectSqlCreate(tablename,lie=None,where=None,group=None,order=None,sort=0):
    sql="SELECT "
    if lie!=None:
        sql=sql+lie+" "
    else:
        sql=sql+"* "
    sql=sql+"FROM "+tablename+" "
    if where!=None:
        sql=sql+"WHERE "+where+" "
    if group!=None :
        sql=sql+"GROUP BY "+group+" "
    if order!=None and sort!=None:
        sql=sql+"ORDER BY "+order+" "
        if sort==0:
            sql=sql+"ASC"
        elif sort==1:
            sql=sql+"DESC"
    return sql

print(SelectSqlCreate(tablename="test"))
print(SelectSqlCreate(tablename="test",lie="id,name"))
print(SelectSqlCreate(tablename="test",lie="id,name",where="name=wangxiaoliang"))
print(SelectSqlCreate(tablename="test",lie="id,name",order="id",sort=1))
print(SelectSqlCreate(tablename="test",lie="id,name",order="id",sort=1))
print(SelectSqlCreate(tablename="test",lie="id,name",group="sex"))
print(SelectSqlCreate(tablename="test",lie="id,name",group="sex",order="id",sort=1))