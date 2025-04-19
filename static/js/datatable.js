$(document).ready(function () {
    $('#tbl_tabla').DataTable({
      dom: 'Bfrtip',
      buttons: [
        { extend: 'print', text: '<i class="fas fa-print"></i> Imprimir', className: 'btn btn-outline-info' },
        { extend: 'pdfHtml5', text: '<i class="fa-solid fa-file-pdf"></i> PDF', className: 'btn btn-outline-danger' },
        { extend: 'csvHtml5', text: '<i class="fa-solid fa-file-csv"></i> CSV', className: 'btn btn-outline-success' },
        { extend: 'excelHtml5', text: '<i class="fa-solid fa-file-excel"></i> Excel', className: 'btn btn-outline-success'}
      ],
      language: {
        url: 'https://cdn.datatables.net/plug-ins/1.13.4/i18n/es-ES.json'
      }
    })
  })

  