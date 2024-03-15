-- range_height.pig: Finds the range of sky ceiling height for each station id

records = LOAD '/home/student3/pig/skyceiling_data.txt' AS (id:chararray, sc:int);
filtered_records = FILTER records BY sc!= 99999;
grouped_records = GROUP filtered_records BY id;

range_result = FOREACH grouped_records {
max_value=MAX(filtered_records.sc);
min_value=MIN(filtered_records.sc);
GENERATE group AS id,(max_value-min_value) AS range;}

DUMP range_result;


