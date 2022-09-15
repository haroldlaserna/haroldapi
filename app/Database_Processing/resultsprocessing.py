import json
from sqlalchemy import Table, Column, Integer, String, text, Float, Time
import datetime
class ResultCreator:
    def __init__(self, engine, conn, meta):
        self.engine = engine
        self.conn = conn
        self.meta = meta


    def create_table(self):
        Circuits = Table("result", self.meta,
                        Column('resultId', Integer, primary_key = True),
                        Column('raceId', Integer),
                        Column('driverId', Integer),
                        Column('constructorId', Integer),
                        Column('number',Integer),
                        Column('grid',Integer),
                        Column('position',Integer),
                        Column('positionText',String),
                        Column('positionOrder',Integer),
                        Column('points',Integer),
                        Column('laps',Integer),
                        Column('time',Time),
                        Column('milliseconds',Integer),
                        Column('fastestLap',Integer),
                        Column('rank',Integer),
                        Column('fastestLapTime',Time),
                        Column('fastestLapSpeed',Float),
                        Column('statusId',Float)
                        )


        self.meta.create_all(self.engine)
        return(Circuits)
    def insert_only_value(self, index, table):
        if index["milliseconds"] != "\\N":
            times = round(float(index["milliseconds"])*1e-3,3)
            times = str(times).split(".")
            mili = times[1]
            times = float(times[0])/60
            times = str(times).split(".")
            second = round(float("0."+times[1])*60)
            times = float(times[0])/60
            times = str(times).split(".")
            minutes = round(float("0."+times[1])*60)
            hours = times[0]
            change_time1 = datetime.time(int(hours), int(minutes),
                                        int(second),int(mili)*1000)

        elif index["milliseconds"] == "\\N":
            index["milliseconds"] = 0
            change_time1 = datetime.time(0, 0, 0)

        if index['fastestLapSpeed'] == "\\N":
            index['fastestLapSpeed'] = 0


        if index["rank"] == "\\N":
            index["rank"] = 0
        if index["position"] == "\\N":
            index["position"] = 0
        if index["fastestLap"] == "\\N":
            index["fastestLap"] = 0




        if index["fastestLapTime"] != "\\N":
            change = index["fastestLapTime"].split(":")
            change1 = change[1].split(".")
            change_time2 = datetime.time(0, int(change[0]),
                                        int(change1[0]),int(change1[1])*1000)
        elif index["fastestLapTime"] == "\\N":
            change_time2 = datetime.time(0, 0, 0)






        insert = table.insert().values(resultId = index["resultId"],
                                       raceId = index["raceId"],
                                       driverId = index["driverId"],
                                       constructorId = index["constructorId"],
                                       number = index["number"],
                                       grid = index["grid"],
                                       position = index["position"],
                                       positionText = index["positionText"],
                                       positionOrder = index["positionOrder"],
                                       points = index["points"],
                                       laps = index["laps"],
                                       time = change_time1,
                                       milliseconds = index["milliseconds"],
                                       fastestLap = index["fastestLap"],
                                       rank = index["rank"],
                                       fastestLapTime = change_time2,
                                       fastestLapSpeed = index["fastestLapSpeed"],
                                       statusId = index["statusId"])

        self.conn.execute(insert)


    def insert_all_data(self, file, table):
        with  open(file) as f:

            for i in range(sum(1 for line in open(file))):
                self.insert_only_value(eval(f.readline()), table)
