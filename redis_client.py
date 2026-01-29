import os
import redis

redis_url = os.getenv('REDIS_URL')

connection = redis.from_url(redis_url)

# Do something here with the connection
print("Connected to Redis at:", redis_url)