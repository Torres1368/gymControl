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