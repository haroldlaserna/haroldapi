from Database_Processing.circuitprocessing import CircuitCreator
from Database_Processing.raceprocessing import  RaceCreator
from Database_Processing.lapprocessing import LapCreator
from Database_Processing.qualifyingprocessing import QualifyingCreator
from Database_Processing.constructorsprocessing import ConstructorCreator
from Database_Processing.driversprocessing import DriverCreator
from Database_Processing.pitstopsprocessing import PitstopCreator
from Database_Processing.resultsprocessing import ResultCreator
from sqlalchemy import create_engine, MetaData

def create_enviroment():
    engine = create_engine('sqlite:///DataBase/racing.db', echo = False)
    conn = engine.connect()
    meta = MetaData()
    return engine, conn, meta

engine, conn, meta = create_enviroment()

def create_data(Creator,file):

    ObjectCreator = Creator(engine,conn,meta)
    Object_table = ObjectCreator.create_table()
    ObjectCreator.insert_all_data(file, Object_table)


    return Object_table, ObjectCreator

def create_query(query):
    t = text(query)
    result = conn.execute(t)
    for row in result:
        print (row)


print(" 1 de 8 Subiendo resutls... ")
file = r'data/Datasets/results.json'
Result_table,  Result = create_data(ResultCreator, file)

print(" 2 de 8 Subiendo pit_stops... ")

file = r'data/Datasets/pit_stops.json'
Pitstop_table, Pitstop = create_data(PitstopCreator, file)

print(" 3 de 8 Subiendo drivers...")

file = r'data/Datasets/drivers.json'
Driver_table, Driver = create_data(DriverCreator, file)

print(" 4 de 8 Subiendo constructors...")
file = r'data/Datasets/constructors.json'
Constructor_table, Constructor = create_data(ConstructorCreator, file)

print(" 5 de 8 Subiendo qualifying...")
print("primera")
file = r'data/Datasets/Qualifying/qualifying_split_1.json'
Qualifying_table, Qualifying = create_data(QualifyingCreator, file)
print("segunda")
file = r'data/Datasets/Qualifying/qualifying_split_2.json'
Qualifying.insert_all_data(file, Qualifying_table)


print(" 6 de 8 lap qualifying...")
print("primera")
file = r'data/Datasets/lap_times/lap_times_split_1.csv'
Lap_table, Lap = create_data(LapCreator, file)
print("segunda")
file = r'data/Datasets/lap_times/lap_times_split_2.csv'
Lap.insert_all_data(file, Lap_table)
print("tercera")
file = r'data/Datasets/lap_times/lap_times_split_3.csv'
Lap.insert_all_data(file, Lap_table)


print(" 7 de 8 Subiendo races...")
file = r'data/Datasets/races.csv'
Race_table, Race = create_data(RaceCreator, file)


print(" 8 de 8 Subiendo circuits...")
file = r'data/Datasets/circuits.csv'
Circuit_table, Circuit = create_data(CircuitCreator, file)
