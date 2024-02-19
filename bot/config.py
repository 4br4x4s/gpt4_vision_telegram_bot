import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", "r") as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token: str = config_yaml["telegram_token"]
openai_api_key: str = config_yaml["openai_api_key"]
openai_api_base: str = config_yaml.get("openai_api_base", None)
allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
new_dialog_timeout: int = config_yaml["new_dialog_timeout"]
enable_message_streaming: bool = config_yaml.get("enable_message_streaming", True)
return_n_generated_images: int = config_yaml.get("return_n_generated_images", 1)
image_size = config_yaml.get("image_size", "1024x1024")
n_chat_modes_per_page: int = config_yaml.get("n_chat_modes_per_page", 5)
mongodb_uri = f"mongodb://mongog:{config_env['MONGODB_PORT']}"

# chat_modes
with open(config_dir / "chat_modes.yml", "r") as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", "r") as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = (
    Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
)
