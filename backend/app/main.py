'''
from fastapi import FastAPI
from app.api import routes as api_routes

app = FastAPI()

app.include_router(api_routes.router)

@app.get("/")s
async def root():
    return {"message": "Hello, world"}
'''

from fastapi import FastAPI
from app.api import routes as api_routes
from fastapi.middleware.cors import CORSMiddleware # For frontend communication

app = FastAPI(
    title="Health Data Research Tool API",
    description="API for the Health Data Research Tool, powered by Sonar.",
    version="0.1.0"
)

# CORS (Cross-Origin Resource Sharing) middleware
# Allows your frontend (running on a different port/domain) to communicate with the backend.
# Be more restrictive in production!
origins = [
    "http://localhost",       # Common default
    "http://localhost:3000",  # Default for create-react-app
    "http://localhost:5173",  # Default for Vite (React)
    # Add your frontend's deployed URL here if applicable
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)

app.include_router(api_routes.router, prefix="/api/v1", tags=["Research"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Health Data Research Tool API!"}

