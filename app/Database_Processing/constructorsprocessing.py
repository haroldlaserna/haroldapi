import json
from sqlalchemy import Table, Column, Integer, String, text, Float, Time
import datetime
class ConstructorCreator:
    def __init__(self, engine, conn, meta):
        self.engine = engine
        self.conn = conn
        self.meta = meta


    def create_table(self):
        Circuits = Table("constructor", self.meta,
                        Column('constructorId', Integer),
                        Column('constructorRef', String),
                        Column('name', String),
                        Column('nationality', String),
                        Column('url',String))


        self.meta.create_all(self.engine)
        return(Circuits)
    def insert_only_value(self, index, table):

        insert = table.insert().values(constructorId = index["constructorId"],
                                       constructorRef = index["constructorRef"],
                                       name = index["name"].title(),
                                       nationality = index["nationality"],
                                       url = index["url"])

        self.conn.execute(insert)


    def insert_all_data(self, file, table):
        with  open(file) as f:

            for i in range(sum(1 for line in open(file))):
                self.insert_only_value(eval(f.readline()), table)
