# Import necessary libraries and modules
import asyncio
import os
from fastapi import APIRouter,status, HTTPException,Depends,Response
import secrets
from fastapi.responses import JSONResponse,FileResponse
from src.v1.server_configs.config.appconfig import auth_user,auth_password
from src.v1.server_configs.config.settings import get_setting
from fastapi.security import HTTPBasic, HTTPBasicCredentials


# Instantiate the settings class
settings=get_setting()

# Instantiate basicAuth
security = HTTPBasic()

# Define the router prefix from the settings module
router = APIRouter(prefix=settings.API_V1_STR)

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    """
    This function sets up the basic auth url protection and returns the credential name.
    
    Args:
        credentials (HTTPBasicCredentials): Basic auth credentials.

    Raises:
        HTTPException: If the username or password is incorrect.

    Returns:
        str: The username from the credentials.
    """
    correct_username = secrets.compare_digest(credentials.username, auth_user)
    correct_password = secrets.compare_digest(credentials.password, auth_password)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect userid or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Define the home router
@router.get("/",status_code=status.HTTP_200_OK)
async def ApiHome(username: str = Depends(get_current_username)):
    """
    This function returns the application details.

    Args:
        username (str): The username from the basic auth credentials.

    Returns:
        dict: A dictionary containing the application details.
    """
    return {"Application": settings.PROJECT_NAME,
            "ApplicationOwner":"DFA23 ML Demo",
            "ApplicationVersion":"1.0.0",
            "API name":settings.PROJECT_NAME,
            "API version":settings.VERSION,
            "ApplicationEngineer":"Sam Ayo"
            }


