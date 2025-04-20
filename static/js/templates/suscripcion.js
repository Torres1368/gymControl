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
        let valorRaw = totalPagarInput.value.trim().replace(',', '.');
        const totalOriginal = isNaN(parseFloat(valorRaw)) || parseFloat(valorRaw) === 0
          ? '0.00'
          : parseFloat(valorRaw).toFixed(2);

        totalPagarInput.dataset.originalValue = totalOriginal;
        totalPagarInput.value = totalOriginal;
      }

      // Resetear monto abonado
      if (montoAbonadoInput) {
        montoAbonadoInput.value = '';
      }

      // Validación y actualización del monto abonado
      if (montoAbonadoInput && totalPagarInput) {
        montoAbonadoInput.addEventListener('input', function () {
          const monto = parseFloat(this.value) || 0;
          const original = parseFloat(totalPagarInput.dataset.originalValue) || 0;

          if (monto > original) {
            iziToast.error({
              title: 'Error',
              message: 'El monto abonado no puede ser mayor al total a pagar.',
              position: 'topRight'
            });
            this.value = '';
            totalPagarInput.value = original.toFixed(2);
            if (estadoSelect) estadoSelect.value = 'pendiente';
            return;
          }

          const nuevoTotal = (original - monto).toFixed(2);
          totalPagarInput.value = nuevoTotal;

          // Validar estado
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

      // Restaurar valor original al cerrar
      if (totalPagarInput && totalPagarInput.dataset.originalValue) {
        totalPagarInput.value = totalPagarInput.dataset.originalValue;
      }

      if (montoAbonadoInput) {
        montoAbonadoInput.value = '';
      }
    });
  });
});

// Eliminar suscripción (sin cambios)
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
            .catch(() => {
              Swal.fire('Error', 'Ocurrió un problema en la solicitud.', 'error');
            });
        }
      });
    }
  });
}
