
class FlatIterator:
    
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

        
    def __iter__(self):
        return self
        