from abc import abstractmethod,ABC

class ApplicationServices(ABC):     # holds contracts -- what are all things we are going to offer

    def add_entity(self):
        pass

    def remove_entity(self):
        pass

    def update_entity(self):
        pass

    def fetch_entity(self):
        pass

    def fetch_all_entities(self):
        pass