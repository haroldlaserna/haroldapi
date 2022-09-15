# API About Data Of History Racing
![alt text](images/racing.jpg)
This API contains a database with 8 tables, which contain too much information
about circuits, types of drivers, the positions occupied by drivers.
The goal of this API is to generate 4 specific queries:
1. Year with the most races.
2. Driver with the most first places.
3. Name of the most run circuit.
4. Driver with the highest number of points in total, whose constructor is of American or British nationality.

Finally, this API can also generate data from the table you want to choose, also choosing the columns you only need and the amount of data.

The data contained in this repository has been normalized using the **sqlalchemy** package, you can find the normalizations made in and the data ingest made in Python in the **Database_Processing** table. To create the normalization you can use the **create_database.py** file. IT IS **NOT NECESSARY** TO EXECUTE IT, the normalization is already created in the **DataBase** folder.

THIS API IS CREATED WITH **fastAPI** PACKAGE IN PYTHON.
## Create Enviroment
To use this API, first need create the environment with virtualenv.
If you have not virtualenv, you con install it with:
```console
pip install virtualenv
```

After installing the previous package, you need to run the shell file,
but first you must give it permissions in the following way:

```console
sudo chmod 777 enviroment.sh
```
To run the environment in the same terminal use **source** as follows:
```console
source enviroment.sh
```
this file create the environment and install the necessary package to run the API.

## Run API

Run the python file **main.py** which is in the app folder as follows:

```console
cd app
```

```console
python3 main.py
```


This creates an URL on your localhost with your API as follows:

<http://127.0.0.1:8000>

## How To Use The API

If you want to see the year with the most races, you have to append to the URL
**/race/maxyear**, and you will see the a list with a dict with your answer.

If you want to see the Driver with the most first places, you have to append
 to the URL **/driver/maxfirst**, and you will see a list with
 a dict with your answer.

 If you want to see the Name of the most run circuit, you have to append
  to the URL **/driver/maxfirst**, and you will see a list with
  a dict with your answer.

 If you want to see the
Driver with the highest number of points in total, whose constructor is of American or British nationality, you have to append
  to the URL **/driver/maxpoints**, and you will see a list with
  a dict with your answer.

In general, If you want to get data of this API, you have to append to the URL
**/table/** and write the name of the following available tables:

| **Table Names**  |
|------------------|
| result           |
| pitstop          |
| driver           |
| constructor      |
| qualifying       |
| laptime          |
| race             |
| circuit          |

for example:

<http://127.0.0.1:8000/table/circuit>

You will see the all data in the table circuit.

If you want to get few data, for example, 7 index you have to use **limit**
as follows:

I want to get only **2** index to the table driver:

<http://127.0.0.1:8000/table/circuit?limit=2>

If you do not want all the columns of the
specific table, you have to use **columns** as follows:

I want to get the colmuns **name**, **datetime** and **url** of the table **race**:

<http://127.0.0.1:8000/table/race?columns=name,datetime,url>

finally,
finally, if you want to combine **limit** and **columns** statements
you will need use the symbol **&** as follows:

I want to get the columns **duration** and **milliseconds** of the table **pitstop**,
but I need only *1* index:

<http://127.0.0.1:8000/table/pitstop?columns=duration,milliseconds&limit=1>
