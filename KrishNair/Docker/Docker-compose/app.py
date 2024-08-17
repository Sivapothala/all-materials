import time
import redis
from flask import Flask
 
app = Flask(__name__)
cache = redis.Redis(host='redis',port=6379)
def get_hit_count():
    retries = 5
    while True:
        try:
            # cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exec:
            if retries == 0:
                raise exec
            retries -= 1
            time.sleep(0.5)



#Routing
@app.route("/",methods=['GET'])
def welcome():
    count = get_hit_count()
    return f"i have been seen {count} times"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)