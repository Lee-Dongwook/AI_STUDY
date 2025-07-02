from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Dict, Any, Optional, Literal, Union

load_dotenv()

def _get_model(config: Dict[str, Any], default:str, key:str):
    if config is None:
        return ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    
    model_type = None

    if 'configurable' in config and key in config['configurable']:
        model_type = config['configurable'].get(key)
    elif key in config:
        model_type = config.get(key)

    if model_type is None:
        model_type = default
    else:
        print(f"경고: 지원되지 않는 모델 유형 '{model_type}'. 기본 모델을 사용합니다.")
        return ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo') # type: ignore
    
