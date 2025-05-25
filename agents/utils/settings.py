from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    GROQ_TEXT_MODEL : str = "llama-3.1-8b-instant"
    MAX_TOKENS : int = 1000
    GROQ_API_KEY : str = ""

settings = Settings()