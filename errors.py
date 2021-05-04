 

class Error:

    def __init__(self,pos_start,pos_end,error_name,details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f"{self.error_name}: {self.details}"
        return result

class IllegalError(Error):
    def __init__(self, pos_start,pos_end,error_name, details):
        super().__init__("Illegal Character", details)