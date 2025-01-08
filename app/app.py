from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

@app.middleware('http')
async def add_csp_header(request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self' https: 'unsafe-inline';"
    return response

# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# To run this application:
# 1. Save it to a file, e.g., `app.py`.
# 2. Run the command: `uvicorn app:app --reload` in your terminal.
# 3. Open your browser and go to `http://127.0.0.1:8000/` to see the message.
