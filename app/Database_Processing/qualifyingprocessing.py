import json
from sqlalchemy import Table, Column, Integer, String, text, Float, Time
import datetime
class QualifyingCreator:
    def __init__(self, engine, conn, meta):
        self.engine = engine
        self.conn = conn
        self.meta = meta


    def create_table(self):
        Circuits = Table("qualifying", self.meta,
                        Column('constructor_Id', Integer),
                        Column('driver_Id', Integer),
                        Column('number', Integer),
                        Column('position',Integer),
                        Column('q1', Time),
                        Column('q2', Time),
                        Column('q3', Time),
                        Column('qualifyId', Integer),
                        Column('raceId', Integer))


        self.meta.create_all(self.engine)
        return(Circuits)
    def insert_only_value(self, index, table):


        change_time1 = index["q1"].split(":")
        change_time2 = index["q2"].split(":")
        change_time3 = index["q3"].split(":")

        def choose_position(change_time):
            if (len(change_time)>2):
                return change_time[2].split("."), change_time
            elif (len(change_time)==1):
                return [0,0], [0,0]
            else:
                return change_time[1].split("."), change_time

        second1, change_time1 = choose_position(change_time1)
        second2, change_time2 = choose_position(change_time2)
        second3, change_time3 = choose_position(change_time3)

        change_time1 = datetime.time(0, int(change_time1[0]),
                                    int(second1[0]),int(second1[1])*1000)
        change_time2 = datetime.time(0, int(change_time2[0]),
                                    int(second2[0]),int(second2[1])*1000)
        change_time3 = datetime.time(0, int(change_time3[0]),
                                    int(second3[0]),int(second3[1])*1000)

        insert = table.insert().values(constructor_Id = index["constructorId"],
                                          driver_Id = index["driverId"],
                                          number = index["number"],
                                          position = index["position"],
                                          q1 = change_time1,
                                          q2 = change_time2,
                                          q3 = change_time3,
                                          qualifyId = index["qualifyId"],
                                          raceId = index["raceId"])

        self.conn.execute(insert)


    def insert_all_data(self, file, table):
        with  open(file) as f:
            data = json.load(f)

            for i in range(len(data)):

                self.insert_only_value(data[i], table)
