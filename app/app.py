from flask import Flask
import redis
import os

app = Flask(__name__)

# Fetch Redis details from environment variables
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))  # Default to 6379
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

# Connect to Azure Redis
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

@app.route('/')
def hello():
    redis_client.incr('hits')
    counter = redis_client.get('hits')
    return f"This webpage has been viewed {counter} time(s)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
