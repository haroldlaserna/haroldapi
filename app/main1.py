import sqlalchemy
from sqlalchemy import create_engine, MetaData, text, inspect, engine



engine = create_engine('sqlite:///DataBase/racing.db', echo = False)
conn = engine.connect()
meta = MetaData(bind=conn)
MetaData.reflect(meta)

def create_query(query):
    t = text(query)
    result = conn.execute(t)
    for row in result:
        print(row)

#create constraint primary keys and foreing keys
#def add_foreign(tablename):



select = "select d.forename || ' ' || d.surname as name , sum(r.points)  as total_points, c.nationality from result as r "
join1 = "inner join driver as d on d.driverId = r.driverId"
join2 = " inner join constructor as c on c.constructorId = r.constructorId"
condition = " where c.nationality IN ('British','American')"
structure = " group by r.driverId order by sum(r.points) DESC"
limits = " limit 300"
query = select + join1 + join2 + condition + structure + limits
print(create_query(query))

print(create_query("pragma table_info(result)"))
print(create_query("pragma table_info(driver)"))
print(create_query("pragma table_info(constructor)"))
