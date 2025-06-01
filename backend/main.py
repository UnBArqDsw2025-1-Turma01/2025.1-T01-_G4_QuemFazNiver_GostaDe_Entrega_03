from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import api_router

app = FastAPI(
    title="QuemFazNiver_GostaDe",
    description="API para gerenciamento de festas, aniversários, convites e sugestões de presentes",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routes from the modular routers
app.include_router(api_router, prefix="/api")

@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint that returns basic API information
    """
    return {
        "message": "Bem-vindo à API QuemFazNiver_GostaDe",
        "version": "1.0.0",
        "documentation": "/docs",
    }

# If you need to add any middleware or event handlers, add them here
@app.on_event("startup")
async def startup_event():
    print("API de Sistema de Eventos iniciada!")

@app.on_event("shutdown")
async def shutdown_event():
    print("API de Sistema de Eventos finalizada!")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
