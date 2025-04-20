document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.modal').forEach(function (modal) {
    modal.addEventListener('shown.bs.modal', function () {
      const id = modal.dataset.suscripcionId;
      const montoAbonadoInput = document.getElementById(`monto_abonado${id}`);
      const totalPagarInput = document.getElementById(`modal_total_pagar${id}`);
      const estadoSelect = document.getElementById(`estado${id}`);
      const fechaInput = document.getElementById(`fecha${id}`);

      // Establecer fecha actual
      if (fechaInput) {
        const today = new Date();
        const yyyy = today.getFullYear();
        const mm = String(today.getMonth() + 1).padStart(2, '0');
        const dd = String(today.getDate()).padStart(2, '0');
        fechaInput.value = `${yyyy}-${mm}-${dd}`;
      }

      // Guardar valor original al abrir el modal
      if (totalPagarInput) {
        let valorRaw = totalPagarInput.value.trim();
        
        // Reemplazar coma por punto (si es necesario)
        valorRaw = valorRaw.replace(',', '.');

        // Verificar y convertir el valor a un número válido
        const totalOriginal = isNaN(parseFloat(valorRaw)) || parseFloat(valorRaw) === 0
          ? '0.00' // Si no es un número válido, mostrar 0.00
          : parseFloat(valorRaw).toFixed(2); // Asegurar que tenga dos decimales
        
        totalPagarInput.dataset.originalValue = totalOriginal;
        totalPagarInput.value = totalOriginal; // Mostrar el valor correctamente formateado
      }

      // Resetear monto abonado
      if (montoAbonadoInput) {
        montoAbonadoInput.value = '';
      }

      // Agregar evento para actualizar total y estado
      if (montoAbonadoInput && totalPagarInput) {
        montoAbonadoInput.addEventListener('input', function () {
          const monto = parseFloat(montoAbonadoInput.value) || 0;
          const rawOriginal = totalPagarInput.dataset.originalValue;
          const original = isNaN(parseFloat(rawOriginal)) ? 0 : parseFloat(rawOriginal);
          const nuevoTotal = (original - monto).toFixed(2); // Asegura que el total se vea con dos decimales

          // Asegurarse de que el valor final sea un número con dos decimales
          totalPagarInput.value = nuevoTotal;

          // Validación de estado
          if (estadoSelect) {
            estadoSelect.value = parseFloat(nuevoTotal) <= 0 ? 'completado' : 'pendiente';
          }
        });
      }
    });

    modal.addEventListener('hidden.bs.modal', function () {
      const id = modal.dataset.suscripcionId;
      const montoAbonadoInput = document.getElementById(`monto_abonado${id}`);
      const totalPagarInput = document.getElementById(`modal_total_pagar${id}`);

      // Restaurar el valor original cuando el modal se cierra
      if (totalPagarInput && totalPagarInput.dataset.originalValue) {
        totalPagarInput.value = totalPagarInput.dataset.originalValue;
      }

      // Resetear monto abonado
      if (montoAbonadoInput) {
        montoAbonadoInput.value = '';
      }
    });
  });
});



function eliminarSuscripcion(url) {
    Swal.fire({
      title: '¿Estás seguro?',
      text: 'Esta acción no se puede deshacer.',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#d33',
      cancelButtonColor: '#3085d6',
      confirmButtonText: 'Sí, eliminar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire({
          title: '¡Atención!',
          text: '¿Estás completamente seguro de eliminar este registro?',
          icon: 'question',
          showCancelButton: true,
          confirmButtonColor: '#d33',
          cancelButtonColor: '#3085d6',
          confirmButtonText: 'Sí, eliminar',
          cancelButtonText: 'Cancelar'
        }).then((result) => {
          if (result.isConfirmed) {
            const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
  
            fetch(url, {
              method: 'DELETE',
              headers: {
                'X-CSRFToken': csrfToken
              }
            })
            .then((response) => {
              if (response.ok) {
                Swal.fire('Eliminado', 'El registro ha sido eliminado.', 'success').then(() => {
                  location.reload();
                });
              } else {
                Swal.fire('Error', 'No se pudo eliminar el registro.', 'error');
              }
            })
            .catch((error) => {
              Swal.fire('Error', 'Ocurrió un problema en la solicitud.', 'error');
            });
          }
        });
      }
    });
  }