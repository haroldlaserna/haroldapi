from sqlalchemy import Table, Time, Column, Integer, String, Date, text, Float
from sqlalchemy import create_engine, MetaData
import datetime


class LapCreator:
    def __init__(self, engine, conn, meta):
        self.engine = engine
        self.conn = conn
        self.meta = meta


    def create_table(self):
        Circuits = Table("laptime", self.meta,
                        Column('race_Id', Integer),
                        Column('driver_Id', Integer),
                        Column('lap', Integer),
                        Column('position',Integer),
                        Column('time', Time),
                        Column('milliseconds', Integer))


        self.meta.create_all(self.engine)
        return(Circuits)

    def insert_only_value(self, index, table):

        index = index.replace('"','')
        index = index.replace('\n','')
        index = index.split(",")
        change_time = index[4].split(":")
        if (len(change_time)>2):
            second = change_time[2].split(".")
        else:
            second = change_time[1].split(".")

        change_time = datetime.time(0, int(change_time[0]),
                                    int(second[0]),int(second[1])*1000)

        insert = table.insert().values(race_Id = index[0],
                                          driver_Id = index[1],
                                          lap = index[2],
                                          position = index[3],
                                          time = change_time,
                                          milliseconds = int(index[5]))

        self.conn.execute(insert)


    def insert_all_data(self, file, table):
        with  open(file) as f:
            index = f.readline()

            for i in range(sum(1 for line in open(file))-1):

                self.insert_only_value(f.readline(), table)
