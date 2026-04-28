from pathlib import Path

ROOT_PATH = Path(__file__).parents[1]
DATA_PATH = ROOT_PATH / "data"
PROMPTS_PATH = ROOT_PATH / "prompt_engineering"
VECTOR_DB_PATH = ROOT_PATH / "knowleadge_base"

#from cohere
EMBEDDING_MODEL = "embed-multilingual-light-v3.0"

MODEL = "openrouter:nvidia/nemotron-3-super-120b-a12b:free"
LLM_JUDGE = "openrouter:/nvidia/nemotron-3-super-120b-a12b:free"

EXPERIMENT_NAME = "animal-guider-bot"
