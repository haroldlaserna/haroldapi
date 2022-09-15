from sqlalchemy import Table, Column, Integer, String, text, Float, Time, Date
import datetime

class DriverCreator:
    def __init__(self, engine, conn, meta):
        self.engine = engine
        self.conn = conn
        self.meta = meta

    def create_table(self):
        Circuits = Table("driver", self.meta,
                        Column('driverId', Integer),
                        Column('driverRef', String),
                        Column('number', Integer),
                        Column('code', Integer),
                        Column('forename', String),
                        Column('surname',String),
                        Column('date',Date),
                        Column('nationality',String),
                        Column('url',String)
                        )


        self.meta.create_all(self.engine)
        return(Circuits)
    def insert_only_value(self, index, table):
        if index["dob"] == "\\N":
            fech = [0, 0, 0]
        else:
            fech = index["dob"].split("-")
        fech = datetime.date(int(fech[0]) ,int(fech[1]), int(fech[1]))
        if index["number"] == "\\N":
            index["number"] = 0
        if index["code"] == "\\N":
            index["code"] = "No Code"
        insert = table.insert().values(driverId = index["driverId"],
                                       driverRef = index["driverRef"],
                                       number = index["number"],
                                       code = index["code"],
                                       forename = index["name"]["forename"],
                                       surname = index["name"]["surname"],
                                       date = fech,
                                       nationality = index["nationality"],
                                       url = index["url"])

        self.conn.execute(insert)


    def insert_all_data(self, file, table):
        with  open(file) as f:

            for i in range(sum(1 for line in open(file))):
                self.insert_only_value(eval(f.readline()), table)
