import json
from sqlalchemy import Table, Column, Integer, String, text, Float, Time
import datetime
class PitstopCreator:
    def __init__(self, engine, conn, meta):
        self.engine = engine
        self.conn = conn
        self.meta = meta


    def create_table(self):
        Circuits = Table("pitstop", self.meta,
                        Column('raceId', Integer),
                        Column('driverId', Integer),
                        Column('stop', Integer),
                        Column('lap',Integer),
                        Column('time', Time),
                        Column('duration', Time),
                        Column('milliseconds', Integer))


        self.meta.create_all(self.engine)
        return(Circuits)
    def insert_only_value(self, index, table):


        change_time1 = index["time"].split(":")
        second2 = str(index["duration"]).split(".")

        if len(second2) == 1:
            second2.append(0)

        if len(second2[0].split(":")) == 1:
            change_time2 = datetime.time(0, 0, int(second2[0]),
                                         int(second2[1])*1000)
        elif len(second2[0].split(":")) == 2:
            minuteseconds = second2[0].split(":")
            change_time2 = datetime.time(0, int(minuteseconds[0]),
                                         int(minuteseconds[1]),
                                         int(second2[1])*1000)


        change_time1 = datetime.time(int(change_time1[0]), int(change_time1[1]),
                                    int(change_time1[2]))


        insert = table.insert().values(raceId = index["raceId"],
                                          driverId = index["driverId"],
                                          stop = index["stop"],
                                          lap = index["lap"],
                                          time = change_time1,
                                          duration = change_time2,
                                          milliseconds = index["milliseconds"])

        self.conn.execute(insert)


    def insert_all_data(self, file, table):
        with  open(file) as f:
            data = json.load(f)

            for i in range(len(data)):
                
                self.insert_only_value(data[i], table)
