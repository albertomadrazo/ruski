from django.db import models

# class Grupo(models.Model):
#     grupo = models.CharField(max_length=1)

#     def creaPartidosRonda(self, selecciones):
#         # Con el array de Selecciones crear los partidos entre ellas
#         juegos = []

#         while selecciones:
#             for i in selecciones:
#                 for j in selecciones:
#                     if i != j:
#                         juegos.append((i, j,))
#                 selecciones.remove(i)
#                 break

#         return juegos

#     def __str__(self):
#         return self.grupo


class Seleccion(models.Model):
    # grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    # escudo = models.ImageField(upload_to='banderas', blank=True, null=True)

    def __str__(self):
        return self.nombre


# class Juego(models.Model):
#     local = Seleccion()
#     visita = Seleccion()
#     resultado = IntegerField()
#     goles = 