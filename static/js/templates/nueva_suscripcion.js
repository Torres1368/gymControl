let precioSeleccionado = 0

$(document).ready(function () {
  // Configuración de Select2 para el cliente
  $('#cliente').select2({
    placeholder: 'Seleccione un cliente',
    allowClear: true,
    width: '100%'
  })

  // Obtener el precio del tipo de pago seleccionado
  $('#tipo_pago').on('change', function () {
    const selectedOption = $(this).find('option:selected')
    precioSeleccionado = parseFloat(selectedOption.data('precio')) || 0
    calcularRestante()
  })

  // Calcular el restante cuando se ingresa el pago inicial
  $('#pago_inicial').on('input', function () {
    const pagoInicial = parseFloat($(this).val()) || 0
    const total = precioSeleccionado

    if (pagoInicial > total) {
      iziToast.error({
        title: 'Error',
        message: 'El pago inicial no puede ser mayor al total a pagar.',
        position: 'topRight'
      })
      $(this).val('')
      $('#total_pagar').val(total.toFixed(2))
      $('#estado').val('pendiente')
      return
    }

    calcularRestante()
  })

  // Función para calcular el restante a pagar
  function calcularRestante() {
    const pagoInicial = parseFloat($('#pago_inicial').val()) || 0
    const restante = precioSeleccionado - pagoInicial
    $('#total_pagar').val(restante.toFixed(2))

    // Actualizar el estado según el restante
    if (restante <= 0) {
      $('#estado').val('activa') // Completado
    } else {
      $('#estado').val('pendiente') // Pendiente
    }
  }

  // Establecer fecha de inicio (hoy) y fecha de fin (un mes después)
  const fechaInicio = $('#fecha_inicio')
  const fechaFin = $('#fecha_fin')
  const fechaHoy = new Date()

  // Ajustar la hora a la zona horaria de Ecuador (UTC-5)
  const offset = 5 * 60 // UTC-5 en minutos
  fechaHoy.setMinutes(fechaHoy.getMinutes() - fechaHoy.getTimezoneOffset() - offset)

  // Establecer la fecha de inicio como la fecha actual (ajustada)
  const fechaInicioString = fechaHoy.toISOString().split('T')[0]
  fechaInicio.val(fechaInicioString)

  // Establecer la fecha de fin como el mismo día del siguiente mes
  fechaHoy.setMonth(fechaHoy.getMonth() + 1)
  const fechaFinString = fechaHoy.toISOString().split('T')[0]
  fechaFin.val(fechaFinString)
})
