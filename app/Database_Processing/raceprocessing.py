from sqlalchemy import Table, DateTime, Column, Integer, String, Date, text, Float
from sqlalchemy import create_engine, MetaData
from datetime import datetime

engine = create_engine('sqlite:///college.db', echo = False)
conn = engine.connect()
meta = MetaData()

class RaceCreator:
    def __init__(self, engine, conn, meta):
        self.engine = engine
        self.conn = conn
        self.meta = meta


    def create_table(self):
        Circuits = Table("race", self.meta,
                        Column('race_Id', Integer, primary_key = True),
                        Column('round', Integer),
                        Column('circuit_Id', Integer),
                        Column('name',String),
                        Column('datetime', DateTime(timezone=True)),
                        Column('url', String))


        self.meta.create_all(self.engine)
        return(Circuits)

    def insert_only_value(self, index, table):

        index = index.replace('"','')
        index = index.replace('\n','')
        index = index.split(",")

        #index[1] = index[1].replace("_"," ")
        #index[1] = index[1].replace("-"," ")
        #index[1] = index[1].title()
        #index[3] = index[3].replace("-"," ")
        #index[3] = index[3].title()
        date = index[5].split("-")

        if index[6] == '\\N':
            time = [0,0,0]
        else:
            time = index[6].split(":")
        d = datetime(int(date[0]), int(date[1]), int(date[2]),
             int(time[0]), int(time[1]), int(time[2]))
        insert = table.insert().values(race_Id = index[0],
                                          round = index[2],
                                          circuit_Id = index[3],
                                          name = index[4],
                                          datetime = d,
                                          url = index[7])

        self.conn.execute(insert)


    def insert_all_data(self, file, table):
        with  open(file) as f:
            index = f.readline()
            for i in range(sum(1 for line in open(file))-1):
                self.insert_only_value(f.readline(), table)
