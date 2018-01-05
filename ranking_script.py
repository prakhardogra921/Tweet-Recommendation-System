__author__ = 'prakhardogra'

from pymongo import MongoClient

client = MongoClient()

db = client.test3

c = db.tweets2

def tweet_recom(list):
    cursor = c.aggregate(
        [
            {
                "$project":
                    {
                        "total":
                            {
                                "$add":
                                    ["$ratio","$rc","$fac"]
                            }
                    }
            }
        ]
    )

    print("\nAggregation complete.")

    for doc in cursor:
        for doc2 in c.find({"_id":doc["_id"]}):
            value = doc["total"]
            hashvalue = 0
            for word in list:
                if word in doc2["text"].split("\n"):
                    hashvalue += 300
            c.update({"_id":doc["_id"]},{"$set":{"value":value+hashvalue}})
    print("Printing recommended tweets according to rank")
    #count = 0
    for doc in c.find({},{"text":1,"value":1,"_id":0}).sort("value",-1):
        print (doc)
        '''
        #if only top 50 results are required
        count += 1
        if count > 50:
            break
        '''
