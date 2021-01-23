'''
Service abstract part given to the client
here abract file for us
Entity is nothing but the items
'''
from abc import abstractmethod,ABC


class ApplicationServices(ABC):     # holds contracts -- what are all things we are going to offer
    @abstractmethod
    def add_entity(self):
        pass

    @abstractmethod
    def remove_entity(self):
        pass

    @abstractmethod
    def update_entity(self):
        pass

    @abstractmethod
    def fetch_entity(self):
        pass

    @abstractmethod
    def fetch_all_entities(self):
        pass

    @abstractmethod
    def get_entity_as_per_cat(self):
        pass