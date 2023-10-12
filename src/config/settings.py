# encoding: utf-8
from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    """
    This class extends the BaseSettings class from FastAPI.
    It contains the project definitions.

    Args:
        None.

    Returns:
        class: extends the settings class.
    """
    
    API_V1_STR: str = "/api/v1"
    VERSION: str = "3.0.2"
    PROJECT_NAME: str = "DFA23 ML Demo Server"

  

def get_setting():
    """
    Return the settings object.

    Args:
        None.

    Returns:
        class: extends the settings class.
    """
    return Settings()

