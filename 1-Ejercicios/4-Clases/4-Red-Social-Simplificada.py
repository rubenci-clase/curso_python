class Publicacion:
    def __init__(self, contenido, usuario):
        self.contenido = contenido
        self.usuario = usuario

    def __str__(self):
        return f"{self.usuario.nombre} publicó: {self.contenido}"


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.amigos = []
        self.publicaciones = []

    def agregar_amigo(self, usuario):
        if usuario not in self.amigos:
            self.amigos.append(usuario)
            print(f"{usuario.nombre} ha sido agregado a tus amigos.")
        else:
            print(f"{usuario.nombre} ya es tu amigo.")

    def realizar_publicacion(self, contenido):
        publicacion = Publicacion(contenido, self)
        self.publicaciones.append(publicacion)

    def ver_publicaciones(self):
        print(f"Publicaciones de {self.nombre}:")
        for publicacion in self.publicaciones:
            print(publicacion)

    def ver_publicaciones_amigos(self):
        print(f"Publicaciones de tus amigos de {self.nombre}:")
        for amigo in self.amigos:
            for publicacion in amigo.publicaciones:
                print(publicacion)


class Amistad:
    def __init__(self, usuario1, usuario2):
        self.usuario1 = usuario1
        self.usuario2 = usuario2
        self.usuario1.agregar_amigo(self.usuario2)
        self.usuario2.agregar_amigo(self.usuario1)

usuario1 = Usuario("Juan")
usuario2 = Usuario("Ana")
usuario3 = Usuario("Carlos")

amistad1 = Amistad(usuario1, usuario2)
amistad2 = Amistad(usuario1, usuario3)

usuario1.realizar_publicacion("Hola, estoy aprendiendo Python!")
usuario2.realizar_publicacion("¡Estoy disfrutando de este curso de Python!")
usuario3.realizar_publicacion("Python es increíble para desarrollo web.")

usuario1.ver_publicaciones()

usuario1.ver_publicaciones_amigos()
