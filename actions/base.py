from abc import ABC, abstractmethod


class Action(ABC):

    @abstractmethod
    def execute(self):
        """Execute the action."""
        pass