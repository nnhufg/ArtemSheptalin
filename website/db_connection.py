# import time
# import logging
# import os
# from dotenv import load_dotenv
# from pymongo import MongoClient

# load_dotenv()

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s - [File: %(pathname)s, Line: %(lineno)d]",
#     filename="logger.log"
# )

# uri = f"mongodb://{os.environ.get('USERNAME')}:{os.environ.get('PASSWORD')}@{os.environ.get('HOST')}:{int(os.environ.get('PORT'))}/{os.environ.get('DATABASE')}"
# max_retries = 5 
# retry_delay = 5 


# def connect_to_mongodb(uri, max_retries, retry_delay):
#     for attempt in range(max_retries):
#         try:
#             client = MongoClient(uri)
#             client.server_info()
#             logging.info("Succussfully connected to MongoDB.")
#             return client
#         except Exception as e:
#             logging.critical(f"Connection ERROR: {e}")
#             if attempt < max_retries - 1:
#                 logging.critical(f"Retry in {retry_delay} seconds...")
#                 time.sleep(retry_delay)
#             else:
#                 logging.critical(f"Still cannot connect to MongoDB. Something went wrong...ERROR: {e}")
#                 raise 


# client = connect_to_mongodb(uri, max_retries, retry_delay)
# db = client['test_database']
# my_collection = db['my_collection']