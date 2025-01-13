from fastapi import FastAPI
from ngrok_test_run import check_ngrok_status, start_ngrok

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    # Check the status of ngrok
    start_ngrok()
    tunnels = check_ngrok_status()
    if tunnels :
        # Start the FastAPI app
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=5000)