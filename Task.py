
from enum import Enum

class Status(Enum) :
    PENDIENTE = 0
    COMPLETADA = 1
    
from Task import Status

class Task :

    def __init__(self, name):
        self.name = name
        self.status = Status.PENDIENTE
        
    def get_status(self) :
         match self.status :
            case Status.PENDIENTE :
                return (self.status, Status.COMPLETADA)
            case Status.COMPLETADA :
                return (self.status, Status.PENDIENTE)
            
    def change_status(self, newStatus) :
        self.status = newStatus
        
    def to_dict(self) :
        return {
            "name" : self.name,
            "status" : self.status.name
        }
    
    @classmethod
    def from_dict(cls, data) :
        task = cls(data["name"])
        task.status =  Status[data["status"]]
        return task
    





