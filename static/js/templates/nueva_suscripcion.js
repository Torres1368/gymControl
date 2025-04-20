let precioSeleccionado = 0

$(document).ready(function () {
  // 1. Inicializa Select2 para el cliente
  $('#cliente').select2({
    placeholder: 'Seleccione un cliente',
    allowClear: true,
    width: '100%'
  })

  // 2. Cuando cambie el tipo de pago, guardamos el precio y recalculamos
  $('#tipo_pago').on('change', function () {
    precioSeleccionado = parseFloat($(this).find('option:selected').data('precio')) || 0
    calcularRestante()
  })

  // 3. Validación y cálculo al ingresar el pago inicial
  $('#pago_inicial').on('input', function () {
    const pagoInicial = parseFloat($(this).val()) || 0
    // Calculamos restante aquí para evitar problemas de decimal
    const restante = precioSeleccionado - pagoInicial

    // Si el restante es negativo, el usuario ha ingresado de más
    if (restante < 0) {
      iziToast.error({
        title: 'Error',
        message: 'El pago inicial no puede ser mayor al total a pagar.',
        position: 'topRight'
      })
      // Restauramos los valores originales
      $(this).val('')
      $('#total_pagar').val(precioSeleccionado.toFixed(2))
      $('#estado').val('pendiente')
      return
    }

    // Si es válido, actualizamos el restante y el estado
    $('#total_pagar').val(restante.toFixed(2))
    $('#estado').val(restante <= 0 ? 'activa' : 'pendiente')
  })

  // 4. Función para recalcular restante (se puede llamar desde otros puntos)
  function calcularRestante() {
    const pagoInicial = parseFloat($('#pago_inicial').val()) || 0
    const restante = precioSeleccionado - pagoInicial
    $('#total_pagar').val(restante.toFixed(2))
    $('#estado').val(restante <= 0 ? 'activa' : 'pendiente')
  }

  // 5. Establecer fechas de inicio y fin automáticamente
  const fechaInicio = $('#fecha_inicio')
  const fechaFin = $('#fecha_fin')
  const fechaHoy = new Date()
  const offset = 5 * 60 // UTC-5 en minutos
  fechaHoy.setMinutes(fechaHoy.getMinutes() - fechaHoy.getTimezoneOffset() - offset)
  fechaInicio.val(fechaHoy.toISOString().split('T')[0])
  fechaHoy.setMonth(fechaHoy.getMonth() + 1)
  fechaFin.val(fechaHoy.toISOString().split('T')[0])
})
