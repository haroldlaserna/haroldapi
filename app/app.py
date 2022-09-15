from fastapi import FastAPI
import sqlalchemy
from sqlalchemy import create_engine, MetaData, text, inspect, engine
import uvicorn
app = FastAPI()

engine = create_engine('sqlite:///racing.db', echo = False)
conn = engine.connect()
meta = MetaData(bind=conn)
MetaData.reflect(meta)

def create_query(query):
    t = text(query)
    result = conn.execute(t)
    finalquery = []
    for row in result:
        finalquery.append(row)
    return finalquery


@app.get("/", tags = ["Root"])
async def hello():
    return "Hola mundo"
@app.get("/table/{tablename}")
async def select_table(tablename, limit = None, columns = None):
    if limit == None:
        limit = ""
    else:
        limit = " limit " + limit
    if columns == None:
        columns = "*"
    query = "select " + str(columns) + " from " + tablename + limit

    return create_query(query)

@app.get("/race/maxyear")
async def maxyearcount():
    year = "strftime('%Y',datetime)"
    count = "count(" + year + ")"
    query = "SELECT " + year + " AS Year, " + count + "AS count_race FROM race GROUP BY " + year
    query = query  + " ORDER BY " + count + " DESC limit 1 "

    return create_query(query)

@app.get("/circuit/max")
async def maxcircuit():
    select = "select c.name, count(c.name) as max_count from race as r "
    join = "inner join circuit as c on r.circuit_Id = c.circuit_Id "
    structure = "group by c.name order by count(c.name) DESC LIMIT 1"
    query = select + join + structure

    return create_query(query)

@app.get("/driver/maxfirst")
async def maxfirstposition():
    concatenate = "select d.forename || ' ' || d.surname as Name, "
    select = concatenate + "count(r.position) as max_first_positions "
    select += "from result as r "
    join = "inner join driver as d on d.driverId = r.driverId "
    condition =  "where r.position = 1"
    structure = condition + " group by r.driverId order by count(r.position) DESC"
    structure += " limit 1"
    query = select + join + structure

    return create_query(query)

@app.get("/driver/maxpoints")
async def maxpointsbritishamerican():
    select1 = "select d.forename || ' ' || d.surname as name, "
    select2 = "sum(r.points)  as total_points, c.nationality from result as r "
    join1 = "inner join driver as d on d.driverId = r.driverId"
    join2 = " inner join constructor as c on c.constructorId = r.constructorId"
    condition = " where c.nationality IN ('British','American')"
    structure = " group by r.driverId order by sum(r.points) DESC"
    limits = " limit 1"
    query = select1 + select2 + join1 + join2 + condition + structure + limits


    return create_query(query)

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=5000, log_level="info")
