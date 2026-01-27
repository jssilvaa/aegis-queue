from pydantic_settings import BaseSettings 

class Settings(BaseSettings): 
        postgres_host: str
        postgres_port: str 
        postgres_user: str 
        postgres_password: str
        postgres_db: str

        redis_host: str 
        redis_port: str 
        
        class Config: 
            env_file = ".env" 

settings = Settings() 
