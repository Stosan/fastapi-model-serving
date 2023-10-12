# Import required modules
import asyncio,gc,time
from fastapi import FastAPI, status
from src.config.settings import get_setting
from fastapi.middleware.cors import CORSMiddleware
import gunicorn
from src.config.appconfig import app_port
from src.api.routes import router as api_router

settings=get_setting()
description = f"""
{settings.API_V1_STR} helps you do awesome stuff. 🚀
"""

gc.collect()

app =  FastAPI(title=settings.PROJECT_NAME,description=description, openapi_url=f"{settings.API_V1_STR}/openapi.json",license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },contact={
        "name": "DFA2023",
        "url": "https://www.example.com/",
        "email": "hello@example.com",
    })

@app.on_event("startup") # event listener for shutdown event
async def startup():
    print("⚡️🚀 DFA23 ML Demo Server::Started")
    #initialize connections to database, Redis
    print("⚡️🏎  DFA23 ML Demo Server::Running")
    

@app.on_event("shutdown") # event listener for shutdown event
async def shutdown():
    """
    Event listener that runs when the application shuts down.

    Prints a message indicating that the application has shut down.
    """
    print("⚡️🚀 DFA23 ML Demo Server::SHUTDOWN")


# include inference router with custom response for HTTP status code 418
app.include_router(api_router, responses={418: {"description": settings.PROJECT_NAME}})


origins = [
    "*",
]

# add middleware to allow CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", status_code=status.HTTP_200_OK) # endpoint for root URL
def Home():
    """
    Returns a dictionary containing information about the application.
    """
    return {
        "ApplicationName": app.title,
        "ApplicationOwner": "DFA23 ML Demo",
        "ApplicationVersion": "1.0.0",
        "ApplicationEngineer": "Sam Ayo",
    }


if __name__ == "__main__":
    # run the application using gunicorn
    gunicorn.run(app, host="0.0.0.0", port=int(app_port))
    while True:
        schedule.run_pending()
        time.sleep(1)
