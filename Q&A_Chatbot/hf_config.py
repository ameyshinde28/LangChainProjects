from pydantic_settings import BaseSettings



class HFconfig(BaseSettings):
    huggingfacehub_api_token: str

    class Config:
        env_file = "hf.env"

hf_config = HFconfig()