from TaskList import TaskList
from Helpers import clear_console
from Helpers import ask_int
from DataPersistance import save_data

class ToDo:
    
    
    def __init__(self):
        self.task_list_grouping = list()
        # data = load_data()
        # self.from_dict(data)
        # self.main_menu()
        
    
    def new_item(self) :
        clear_console()
        new_task_list_name = input("Por favor, intruduzca el nombre de la lista de tareas: \n\n")
        new_task_list = TaskList(new_task_list_name, self)
        self.task_list_grouping.append(new_task_list)
        save_data(self)
        new_task_list.ask_new_task()
  

    def display_titled_tasklist(self):
        clear_console()
        print("----TO DO LIST---\n")
        self.show_task_list()
        

    def main_menu(self):
        
        while True:
            self.display_titled_tasklist()
            print("Seleccione una opción: ")
            if len(self.task_list_grouping) == 0 :
                answer = input("N: Nueva Lista de Tareas\n \n").upper()
            else:
                answer = input("N: Nueva Lista de Tareas \nA: Abrir lista de tareas \nE: Editar nombre lista de tareas \nB: Borrar lista de tareas \nS: Salir \n \n").upper()
                
            match answer :
                case "N": 
                    self.new_item()
                case "A":
                    self.view_item()
                    
                case "E":
                    self.edit_item()
                case "B":
                    self.delete_item()        
                case "S" :
                    exit()
                    break
                case _:
                    print("Valor no válido.")

    def view_item(self):
        list_index = self.select_list("Introduzca el número de la lista de tareas que desea visualizar: \n\n")
        task_list = self.task_list_grouping[list_index]
        #####
        clear_console()
        task_list.display_task_menu()
                

    def delete_item(self):
        list_index = self.select_list("Introduzca el número de la lista de tarea que desea borrar: \n\n")
        removed_task_name = self.task_list_grouping.pop(list_index).name
        #Remove from saved data
        clear_console()
        print(f"{removed_task_name} se ha borrado de la lista")

    def edit_item(self):
        list_index = self.select_list("Introduzca el número de la lista de tareas que desea editar: \n\n")
        previous_item_name = self.task_list_grouping[list_index].name
        #####
        clear_console()
        print(f"Has seleccionado {previous_item_name}.")
        new_item_name = input("¿Qué nombre desea ponerle?\n \n")
        self.task_list_grouping[list_index].name = new_item_name
        #edit in saved data
        ####
        clear_console()
        print(f"{previous_item_name} cambiado satisfactoriamente a {new_item_name}")

    def select_list(self, message):
        clear_console()
        while True :
            self.show_task_list()
            user_selected_num = ask_int(message)
            
            if 1 <= user_selected_num <= len(self.task_list_grouping) :
                break
            
            print("Valor no encontrado")
        
        return user_selected_num - 1

    def show_task_list(self):
        if len(self.task_list_grouping) > 0 :
            print("LISTAS DE TAREAS: \n")
          
            for index, task_list in enumerate(self.task_list_grouping, start=1) :
                print(f"{index}. {task_list.name}")
        else :
            print("(Ningún elemento en la lista)")
        print("-----------------\n")
        
    def to_dict(self) :
        return {
            "task_lists" : [
                task_list.to_dict()
                for task_list in self.task_list_grouping]
        }
    @classmethod
    def from_dict(cls, data) :
        todo = cls()
        todo.task_list_grouping = [
                TaskList.from_dict(task_data, todo)
                for task_data in data["task_lists"]
                ]
        return todo