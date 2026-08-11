import json
from dataclasses import asdict


from app.models import MovementScript, MovementConfig


def save_to_json(file_path: str, movement_script: MovementScript) -> None:
    data_dict = asdict(movement_script)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=2)


def load_config_from_json(file_path: str) -> MovementConfig:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return MovementConfig.model_validate(data)
