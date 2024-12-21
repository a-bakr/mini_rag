from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseSignal
import re
import os


class DataController(BaseController):

    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes
    
    def validate_uploaded_file(self, file: UploadFile):
        
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value
    
    def generate_unique_filename(self, orig_file_name: str, project_id:str):

        project_path = ProjectController().get_project_path(project_id)
        cleaned_file_name = self.get_clean_file_name(orig_file_name)

        file_name = ""
        new_file_path = ""
        while True:
            random_key = self.generate_random_string()
            file_name = random_key +"_"+ cleaned_file_name
            new_file_path = os.path.join(project_path, file_name)

            if not os.path.exists(new_file_path):
                break
        
        return new_file_path, file_name

    def get_clean_file_name(self, orig_file_name:str):
        # remove any special characters, except underscore and.
        return re.sub(r'[^\w.]', '', orig_file_name.strip()).replace(" ", "_")