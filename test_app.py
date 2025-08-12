import requests
import threading
import time
import uvicorn
from main import app

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)


thread = threading.Thread(target=run_server, daemon=True)
thread.start()


time.sleep(2)


res = requests.get("http://127.0.0.1:8000")
assert res.status_code == 200
assert res.json()["message"] == "Hello from GitHub Actions!"
print("✅ Test passed successfully!")
