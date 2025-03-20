class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
    for tarea in self.tareas:
        if tarea.estaLista():
            print(f"[X] {tarea.obtenerNombre()}" )
<<<<<<< HEAD

=======
        
>>>>>>> 50f3793b6bbc448731bb71d032190f217e7cc7bc
            print(f"[ ] {tarea.obtenerNombre()}" )
