from __future__ import annotations
from abc import ABC, abstractmethod
#product Abstract
class DbConector(ABC):
    def __init__(self, ConnectionString):
        self.ConnectionString = ConnectionString
    @abstractmethod
    def Connect(self):
        pass