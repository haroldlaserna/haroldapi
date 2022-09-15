from sqlalchemy import Table, Column, Integer, String, text, Float

class CircuitCreator:
    def __init__(self, engine, conn, meta):
        self.engine = engine
        self.conn = conn
        self.meta = meta


    def create_table(self):

        Circuits = Table("circuit", self.meta,
                        Column('circuit_Id', Integer, primary_key = True),
                        Column('short_name', String),
                        Column('name', String),
                        Column('location', String),
                        Column('country',String),
                        Column('latitude', Float),
                        Column('longitude', Float),
                        Column('alt', Integer),
                        Column('url', String))
        self.meta.create_all(self.engine)
        return(Circuits)

    def insert_only_value(self, index, table):
        index = index.replace('"','')
        index = index.replace('\n','')
        index = index.split(",")
        index[1] = index[1].replace("_"," ")
        index[1] = index[1].replace("-"," ")
        index[1] = index[1].title()
        index[3] = index[3].replace("-"," ")
        index[3] = index[3].title()
        insert = table.insert().values(circuit_Id = index[0],
                                          short_name = index[1],
                                          name = index[2],
                                          location = index[3],
                                          country = index[4],
                                          latitude = index[5],
                                          longitude = index[6],
                                          alt = index[7],
                                          url = index[8])

        self.conn.execute(insert)

    def insert_all_data(self, file, table):
        with  open(file) as f:
            index = f.readline()

            for i in range(sum(1 for line in open(file))-1):
                self.insert_only_value(f.readline(), table)
