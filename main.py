from fastapi import FastAPI

app = FastAPI(title="TestApp")

@app.get('/items')
async def list_items():
    return []

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/test_data')
async def test_data():
    return {"data": "This is test data"}
