from dotenv import load_dotenv
import os
from pathlib import Path
import toml

load_dotenv()

project_file = toml.load(Path(Path.cwd(), "..", "pyproject.toml"))
project_data = project_file["tool"]["poetry"]

CONFIG: dict[str, any] = {  # type: ignore
    "env": os.getenv("ENV"),
    "is_dev": os.getenv("ENV") == "development",
    "is_prod": os.getenv("ENV") == "production",

    "host": "0.0.0.0",
    "port": os.getenv("PORT"),
    "allowed_origins": ["localhost", os.getenv("CONSUMER_URI")],

    "app_name": project_data["name"],
    "app_desc": project_data["description"],
    "app_version": project_data["version"],
}
