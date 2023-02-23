class Empleado:
    def __init__(self, nombre_completo, nombre_proyecto):
        self.nombre = nombre_completo
        self.proyecto = nombre_proyecto
        
    @staticmethod
    def tarea_a_realizar(nombre_proyecto):
        if nombre_proyecto == "Electromagnetismo":
            tarea = ['tarea_1', 'tarea_2', 'tarea_3']
        else:
            tarea = ['tarea_1']
        return tarea


    def trabajar(self):
        self.tareas = self.tarea_a_realizar(self.proyecto)
        if len(self.tareas)>1:
            print(self.nombre)
            for tarea in self.tareas:
                print(tarea, "completada") 
        else:
            print(self.nombre)
            print(self.tareas, "completada")        


empleado = Empleado("Micaela", "Elecromagnetismo")
empleado.trabajar()