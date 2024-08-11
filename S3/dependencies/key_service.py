import uuid
from datetime import datetime


def generate_image_key(extension: str) -> str:
    unique_id = uuid.uuid4()

    current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")

    key = f"{current_time}_{unique_id}.{extension}"

    return key


def generate_folder_key(folder_name: str) -> str:
    unique_id = uuid.uuid4()

    current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")

    key = f"{current_time}_{unique_id}.{folder_name}"

    return key
