from fastapi import FastAPI
from routes import router
import database

app = FastAPI()

# Include routes
app.include_router(router)

# Initialize database
database.init_db()

@app.get("/")
def home():
    return {"message": "Dream11 Automation API is running"}
