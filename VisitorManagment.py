from Visitor import Visitor

class VisitorManagment:
    """class to represent visitor managment"""

    #constructor:
    def __init__(self, numOfvisitors):
        self.numOfvisitors = numOfvisitors

    #setter getter functions:
    def set_numOfvisitors(self, numOfvisitors):
        self.numOfvisitors = numOfvisitors

    def get_numOfvisitors(self):
        return self.numOfvisitors

    def register_visitor(self, new_visitor): #function to register visitors.
        self.numOfvisitors += 1

    def remove_visitor(self, visitor): #function to remove visitors.
        if self.numOfvisitors  > 0:
            self.numOfvisitors  -= 1

    def update_num_of_visitors(self, numOfvisitors): #function to update the number of visitors in the museum.
        self.numOfvisitors  = num_of_visitors