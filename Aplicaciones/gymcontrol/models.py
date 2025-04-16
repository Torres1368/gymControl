from django.db import models

# Create your models here.
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True,unique=True,  null=True)
    telefono = models.CharField(max_length=100, blank=True, unique=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} , {self.apellido}"
    

class TipoPago(models.Model):
    id = models.AutoField(primary_key=True)
    TIPO_CHOICES = [('diario', 'Diario'),('mensual', 'Mensual'),]
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)    
    descripcion= models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tipo

class Suscripcion(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ESTADO_CHOICES = [('activa', 'Activa'),('vencida', 'Vencida'),('pendiente', 'Pendiente'),] #add por ahora 
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')#add por ahora
    tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    pago_inicial=models.DecimalField(max_digits=10, decimal_places=2)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cliente.nombre , self.cliente.apellido, self.fecha_fin

class Abono(models.Model):
    id = models.AutoField(primary_key=True)
    Suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    monto_abonado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Suscripcion.cliente.nombre , self.Suscripcion.cliente.apellido, self.fecha
    
