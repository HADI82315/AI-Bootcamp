from abc import ABC, abstractmethod 
from typing import Any, List 
import re
 
class PipelineStep(ABC): 
    """ 
    An abstract base class representing a single step in a processing 
    pipeline. 
    """ 
    @abstractmethod 
    def process(self, data: Any) -> Any: 
        """ 
        Processes the input data and returns the result. 
        This method must be implemented by all concrete subclasses. 
        """ 
        pass
    
class DataLoader(PipelineStep): 
    """ 
    Loads data from a text file, returning a list of lines. 
    """ 
    def process(self, filepath: str) -> List[str]: 
        """ 
        Reads a file from the given filepath and returns its lines as a 
        list of strings. 
        Handles FileNotFoundError and other potential exceptions. 
        """ 
        try:
            with open(filepath,mode="r") as file:
                self.lines = file.readlines()
        except FileNotFoundError:
            print("Error: File not found.")
        except PermissionError:
            print("Error: No permission to read the file.")
        except UnicodeDecodeError:
            print("Error: Encoding problem. Try a different encoding.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            return [line.strip() for line in self.lines]
        
        exit()
        
class Preprocessor(PipelineStep): 
    """ 
    Cleans a list of text strings by converting to lowercase, removing 
    punctuation, 
    and stripping extra whitespace. 
    """ 
    def __init__(self, punctuation_to_remove: str = r'[^\w\s]'): 
        self.punctuation_pattern = re.compile(punctuation_to_remove) 
 
    def process(self, data: List[str]) -> List[str]: 
        """ 
        Applies cleaning steps to each string in the input list. 
        """ 
        return [re.sub(r"\s{2,}"," ",self.punctuation_pattern.sub("",line.strip().lower())) for line in data]
        