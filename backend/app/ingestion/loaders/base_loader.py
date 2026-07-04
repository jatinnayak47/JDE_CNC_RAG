from abc import ABC
from abc import abstractmethod


class BaseLoader(ABC):

    @abstractmethod
    def load(self, file_path: str):
        pass