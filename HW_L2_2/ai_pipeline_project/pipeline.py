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
        try:
            return [re.sub(r"\s{2,}"," ",self.punctuation_pattern.sub("",line.strip().lower())) for line in data]
        except Exception as e:
            print(f"Unexpected error: {e}")
            exit()

class Analyzer(PipelineStep): 
    """ 
    Analyzes the text data to compute basic statistics. 
    """ 
    def process(self, data: List[str]) -> dict: 
        """ 
        Calculates total lines, average words per line, and number of 
        unique words. 
        """ 
        statistics = {}
        statistics["total_lines"] = len(data)
        words = " ".join(data).split(sep=" ")
        try:
            statistics["avg_length"] = len(words)/statistics["total_lines"]
        except ZeroDivisionError:
            print("empty file")
            exit()
        statistics["unique_words"] = len(set(words))
        
        return statistics
    
class ReportGenerator: 
    """ 
    Generates and outputs reports from the analysis statistics. 
    """ 
    def print_to_console(self, stats: dict): 
        """ 
        Prints the statistics in a formatted way to the console. 
        """ 
        for key,value in stats.items():
            if isinstance(value,float):
                print(f"{key}: {value:.2f}")
            else:
                print(f"{key}: {value}")
 
    def save_to_file(self, stats: dict, filepath: str): 
        """ 
        Saves the statistics in a formatted way to a text file. 
        """ 
        try:
            with open(filepath, mode="w") as file:
                for key,value in stats.items():
                    if isinstance(value,float):
                        file.write(f"{key}: {value:.2f}\n")
                    else:
                        print(f"{key}: {value}\n")
        except Exception as e:
            print(f"Unexpected error: {e}")