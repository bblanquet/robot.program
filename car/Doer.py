from abc import ABC, abstractmethod
from ActionKind import ActionKind


class Doer(ABC):
    def __init__(self):
        self._is_busy = False
        
    def do(self, action: ActionKind):
        if self._is_busy == False:
            self._is_busy = True
            self._execute(action)
            self._is_busy = False
        else:
            print(f'{action} is ignored. the action is already processing.')
        
    def stop(self):
        pass
        
    @abstractmethod
    def _execute(self, action: ActionKind):
        pass