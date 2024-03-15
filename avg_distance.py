
from pyspark import SparkContext
import re
import sys

def main():

   # Create the SparkContext
   sc = SparkContext(appName='AvgDistance')

   # Read the input file into an RDD
   input_rdd = sc.textFile("/user/hadoop/input/")
   
   # Filter out the records with invalid quality and temperature
   filtered_rdd = input_rdd.filter(lambda line: line[78:84]!="999999" and  int(line[84:85]) in [0, 1, 4, 5, 9 ])
 
   # Extract id and dist from the filtered record
   id_dist_rdd = filtered_rdd.map(lambda line: (line[4:10], int(line[78:84])))

   # Calculate the avg temperature for each year
   avg_dist_rdd = id_dist_rdd.groupByKey().mapValues(lambda var1: sum(var1)/len(var1) )

   # Save the output into a output file
   avg_dist_rdd.saveAsTextFile("/user/hadoop/projectoutputspark2")
  
   # Stop the SparkContext
   sc.stop()

   
if __name__ == '__main__':
   main()
  

   

  