# For testing and debugging of local objects, run
# "pip install pyspark=X.Y.Z", where "X.Y.Z"
# matches the version of PySpark
# on your target clusters.
from pyspark.sql import SparkSession

from pyspark.sql.types import *
from datetime import date

spark = SparkSession.builder.appName("dbx-demo-cicd_task2").getOrCreate()





spark.sql('USE demo_a0')

df_temps = spark.sql("SELECT * FROM demo_dbx_table " \
   "WHERE AirportCode != 'BLI' AND Date > '2021-04-01' " \
   "GROUP BY AirportCode, Date, TempHighF, TempLowF " \
   "ORDER BY TempHighF DESC")
df_temps.show(1)

# Results:
#
# +-----------+----------+---------+--------+
# |AirportCode|      Date|TempHighF|TempLowF|
# +-----------+----------+---------+--------+
# |        PDX|2021-04-03|       64|      45|
# +-----------+----------+---------+--------+

# Clean up by deleting the table from the cluster.
#spark.sql('DROP TABLE demo_dbx_table')