import yaml
from pathlib import Path

def load_prompts() -> dict:
    prompts_file = Path(__file__).parent / "prompts.yaml"
    with open(prompts_file, 'r', encoding='utf-8') as file:
        prompts = yaml.safe_load(file)
    return prompts