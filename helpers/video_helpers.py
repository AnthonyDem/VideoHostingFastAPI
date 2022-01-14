import shutil
from uuid import uuid4

from fastapi import UploadFile, File


class FileHelper(object):
    def __init__(self, user_id: int, file: UploadFile = File(...)):
        self.file = file
        self.user_id = user_id

    def write_file(self) -> None:
        filepath = f'media/{self.user_id}/{uuid4()}_{self.file.filename}'
        with open(filepath, 'wb') as file_obj:
            shutil.copyfileobj(self.file.file, file_obj)