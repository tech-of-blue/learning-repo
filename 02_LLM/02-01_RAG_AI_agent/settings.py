import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# .env ファイルを読み込む
path_env="C:\\Users\\Yuichi Katogi\\.env"
load_dotenv(path_env)



class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    # 環境変数を取得
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    langsmith_tracing_v2 = os.getenv("LANGCHAIN_TRACING_V2")
    langsmith_endpoint = os.getenv("LANGSMITH_ENDPOINT")
    langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
    langsmith_project = os.getenv("LANGSMITH_PROJECT")

    # for Application
    openai_smart_model: str = "gpt-4o-mini"
    openai_embedding_model: str = "text-embedding-3-small"
    #anthropic_smart_model: str = "claude-3-5-sonnet-20240620"
    temperature: float = 0.0
    #default_reflection_db_path: str = "tmp/reflection_db.json"

    def __init__(self, **values):
        super().__init__(**values)
        self._set_env_variables()

    def _set_env_variables(self):
        for key in self.__annotations__.keys():
            if key.isupper():
                os.environ[key] = getattr(self, key)