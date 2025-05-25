from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    GROQ_TEXT_MODEL : str = "meta-llama/llama-4-scout-17b-16e-instruct"
    MAX_TOKENS : int = 1000
    GROQ_API_KEY : str = ""
    HUGGINGFACE_EMBEDDING_MODEL : str = "sentence-transformers/all-mpnet-base-v2"
    HUGGINGFACE_EMBEDDING_ARGS : dict = {'device' : 'cpu'}

settings = Settings()