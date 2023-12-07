from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Reserva(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    )

    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    correo_electronico = models.EmailField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True)

    class Meta:
        db_table = 'django_reservas'

    def __str__(self):
        return f"{self.nombre} - {self.fecha_reserva} {self.hora_reserva}"