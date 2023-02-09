import json


class Config():
    
    
    def __init__(self, file):
        
        self.file = file
        self.conf = None
        
        with open(self.file, 'r') as file:
            self.conf = json.load(file)


    def write_file(self, conf_json = None):
        """add the settings of the app """
        with open(self.file, "w") as file:
            json.dump(conf_json, file)
            
    def read_file(self):
        data = None
        with open(self.file, "r") as file:
            data = json.load(file)
        return data
            
    