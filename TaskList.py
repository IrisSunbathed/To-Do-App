from Task import Task
from Helpers import clear_console
from Helpers import ask_int
from DataPersistance import save_data


class TaskList :
    
    def __init__(self, name, to_do):
        self.name = name
        print(name)
        # self.tasks = dict()
        self.task_list = list()
        self.to_do = to_do
    
        
    def new_task(self) :
        task_name = input("¿Qué nombre deasea darle a la tarea? \n\n")
        new_task = Task(task_name)
        self.task_list.append(new_task)
        save_data(self.to_do)
        clear_console()
        print(f"{task_name} creada satisfactoriamente.")

    def display_task_menu(self):
        
        while True:
            self.display_tasks()
            print("Seleccione una opción:")
            if len(self.task_list) == 0 :
                answer = input("\nN: Nueva Tarea \nR: Retroceder \n\n").upper()
                match answer :
                    case "N": 
                        clear_console()
                        self.new_task()
                  
                    case "R":
                        break
                    case _:
                        print("Valor no válido.")
            else:
                answer = input("\nN: Nueva Tarea \nE: Editar tarea \nB: Borrar tarea \nR: Retroceder \n\n").upper()
                match answer :
                    case "N":
                        clear_console()
                        self.new_task()
                    case "E":
                        self.edit_task()
                    case "B":
                        self.remove_task()
                        save_data(self.to_do)
                    case "R":
                        break
                    case _:
                        print("Valor no válido.")

    def display_tasks(self):
        
        dash = "-" *  len(self.name)
        print(f"\n{dash}\n",)
        print(f"{self.name}".upper())
        print(f"{dash}")
        if len(self.task_list) > 0 :
            for index, task in enumerate(self.task_list, start=1) :
                print(f"{index}. {task.name} \n ({task.status.name})")
        else :
            print("(Ningún elemento en la lista)")
        print(f"{dash}")

    def remove_task(self):
        task_index = self.select_task("borrar")
        removed_task_name = self.task_list.pop(task_index).name
        clear_console()
        print(f"{removed_task_name} se ha borrado correctamente.")

    def edit_task(self):
        task_index = self.select_task("editar")
        
        previous_task_name = self.task_list[task_index].name
        clear_console()
        print(f"Has seleccionado {previous_task_name}.")
            
        while True :
            answer = input("¿Desea actualizar el nombre o el estado? \nN: Nombre \nE: Estado \nC: Cancelar \n\n").upper()
            match answer:
                case "N":
                    clear_console()
                    self.edit_name(task_index, previous_task_name)
                    save_data(self.to_do)
                    
                    break
                case "E":
                    clear_console()
                    self.edit_status(task_index, previous_task_name)  
                    save_data(self.to_do)
                    break
                case "C":
                    clear_console()
                    break
                case _ :
                    print("Valor no válido")
        

    def select_task(self, action):
        clear_console()
        while True :
            self.display_tasks()
            user_input = ask_int(f"Introduzca el número de la tarea que desee {action}: \n\n")
           
            
            if  1 <= user_input <= len(self.task_list) :
                break
            
            print("Valor no encontrado")
        return user_input - 1

    def edit_status(self, task_index, previous_task_name):
        while True :
            from_status, to_status = self.task_list[task_index].get_status()
            answer = input(f"¿Desea cambiar del estado {from_status.name} a {to_status.name}? S/N \n \n" ).upper()
            match answer :
                case "S" :
                    self.task_list[task_index].change_status(to_status)
                    clear_console()
                    print(f"{previous_task_name} cambiado su estado satisfactoriamente a completado")
                    #edit in saved data
                    break
                case "N" :
                    break
                case _:
                    print("Valor no válido")
      

    def edit_name(self, taskNum, previous_task_name):
        
        new_task_name = input(f"¿Qué otro nombre desea asignarle a {previous_task_name}?\n \n")
        self.task_list[taskNum].name = new_task_name
        #edit in saved data
        clear_console()
        print(f"{previous_task_name} cambiado satisfactoriamente a {new_task_name}")
       
        
    def ask_new_task(self) :
        clear_console()
        while True :
            answer = input(f"¿Desea añadir una tarea a {self.name}? S/N \n\n").upper()
            
            match answer:
                case "S" :
                    clear_console()
                    self.new_task()
                    self.display_task_menu()
                    break
                case "N" :
                    break
                case _:
                    print("Valor no válido.")
                    
    def to_dict (self) :
        return {
            "name" : self.name,
            "Tasks" : [
                task.to_dict()
                for task in self.task_list
            ]
        }
    
    @classmethod
    def from_dict(cls, data, todo) :
        tasklist = cls(data["name"], todo)
        tasklist.task_list = [
                Task.from_dict(task_data)
                for task_data in data["Tasks"]
                ]
        return tasklist
        