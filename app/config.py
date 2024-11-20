from email.policy import default
from dotenv import load_dotenv
import aiofiles
from pathlib import Path
import os
load_dotenv()
def save(str1, str2="uploaded", default = ""):
    return (str1 if str1 else default) + "/" + str2
dir = save(os.getenv("BASE_DIR"), "uploaded_files")