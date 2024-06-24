import redis
from rq import Queue

r_conn = redis.Redis(host="localhost", port=6379)
queue = Queue(connection=r_conn)
