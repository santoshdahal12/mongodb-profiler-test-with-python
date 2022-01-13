# mongodb-with-python-bulk-insert

To install mongodb in macos, follow this link https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/

1. `brew tap mongodb/brew`
2. `brew install mongodb-community@5.0`
3. Run mongo db as background service with `mongod --config /usr/local/etc/mongod.conf --fork`
4. To verify that MongoDB is running, perform one of the following:
   If you started MongoDB manually as a background process:
   `ps aux | grep -v grep | grep mongod` will output `mongod`
5. Install mongoDB Compass for a handy UI from here https://docs.mongodb.com/compass/current/install/
6. Open Mongodb Compass and choose localhost as an option to connect. 