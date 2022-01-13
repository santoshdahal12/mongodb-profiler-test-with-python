# mongodb-profiler_test_with_python

This project is to do performance test of mongo db and understand query performance. 

This project does bulk insert of 500k records in local mongo db. Each of the records are randomly assigned to a record id from a list of 30k UUIDs generated.
This is to make sure there are random number of records linked to an id and not all of them are unique.

They are all dumped to mongo db local. Each events are assigned to a random created time stamp between now and 1 year ago.

The performance testing is of a simple find by id query that also does sort based on datetime. 

The document schema is :
`
{"id":uuid,
  "fname":"random-name"
   "lname":"random-name",
   "date":{"created":date-time-stamp-str}
}
`

The db name created is : `testdatabase`
The collection name is `records_collection`
While testing, it was found that, 

1. without index, Mongo Db was doing full collection scan.

2. By creating an index of date-time (date.created field), it was also doing high number of document scan. This is because we are filtering by id but index is wrong. The document scan is still lower than without index.
3. By creating an index by id, the total document scan was lowered to number of records that particular id had. Hence,  this is the most efficient index.

To analyze how many documents were scanned for a query, we can run mongo profiler in local.

The below steps tells how to section of installing MongoDb in MacOS plus running mongo db profiler.

To install mongodb in macos, follow this link https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/

1. `brew tap mongodb/brew`
2. `brew install mongodb-community@5.0`
3. Run mongo db as background service with `mongod --config /usr/local/etc/mongod.conf --fork`
4. To verify that MongoDB is running, perform one of the following:
   If you started MongoDB manually as a background process:
   `ps aux | grep -v grep | grep mongod` will output `mongod`
5. Install mongoDB Compass for a handy UI from here https://docs.mongodb.com/compass/current/install/
6. Open Mongodb Compass and choose localhost as an option to connect. 

# Mongo Db profiler

First make sure mongodb is properly installed.

1. start the mongo shell by running `mongo` in a mac terminal
2. change the current db to the database we are trying to analyze using `use testdatabase`
3. Get the current setting of profiler by running `db.getProfilingStatus()`
4. This will output something like this based on what the profiler level was set `{ "was" : 0, "slowms" : 100, "sampleRate" : 1 }`
5. Set the profiler to level 2 to get the documents scanned result with `db.setProfilingLevel(2)`
6. After each time u run a query in mongo, we can run different commands in profiler to get analyse the result.
7. for example: `db.system.profile.find({"docsExamined":{$gt:0}})` gives the query execution details of all query as we are asking all queruies detaisl that scanned document greater than 0.
8. By the analyzing the json of above reult , we can check if our indexes are doing good. 