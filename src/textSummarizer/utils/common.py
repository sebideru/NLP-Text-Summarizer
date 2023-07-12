import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    
    """Read a YAML file and return a ConfigBox object.
    args:
    path: Path to the YAML file.

    Raises:
    valueError: If the file is not a valid YAML file.
    Returns: A ConfigBox object.
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is not a valid yaml file.")
    except Exception as e:
            raise e       

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    """Create list of directories.
     
     args:
        path_to_dicrectories(list): List of path directories
        ignore_log(bool,optional): ignore if multiple dirs is to be created.Defaults to False.
     """ 

    for path in path_to_directories:
     os.makedirs(path,exist_ok=True)
     if verbose:
          logger.info(f"created directory at: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file.
    args:
    path(Path): Path to the file.
    Returns:
        str:size in KB
    """

    size_in_kb = round(os.path.getsize(path)/1024,2)
    return f"~{size_in_kb} KB"