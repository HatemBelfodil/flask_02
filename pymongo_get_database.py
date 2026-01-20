from pymongo import MongoClient
def get_database(db_name):
   #uri = "mongodb+srv://hatembelfodil213_db_user:IRtPSf2E5uIfu7gM@cluster0.lw1eea7.mongodb.net/?appName=Cluster0"

   user="hatembelfodil213_db_user"
   pwd = "IRtPSf2E5uIfu7gM"
   cluster_url = "cluster0.lw1eea7.mongodb.net"
   database_name=""
   connection_option="appName=Cluster0"

   uri_patter="mongodb+srv://<username>:<password>@<cluster-url>/<database-name>?<options>"
   uri_patter=uri_patter.replace("<username>", user)
   uri_patter=uri_patter.replace("<password>", pwd)
   uri_patter=uri_patter.replace("<cluster-url>", cluster_url)
   uri_patter = uri_patter.replace("<database-name>",database_name)
   uri_patter=uri_patter.replace("<options>", connection_option)

   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(uri_patter)

   # Send a ping to confirm a successful connection
   try:
      client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
   except Exception as e:
      print(e)

   # Create the database for our example (we will use the same database throughout the tutorial
   return client[db_name]
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()