$(document).ready(function() {
    // Inicializa Select2 en los select
    $('#cliente, #tipo_pago').select2();

    // Valida el formulario
    $("#frm_suscripcion").validate({
        rules: {
            "cliente": {
                required: true 
            },
            "tipo_pago": {
                required: true 
            },
            "pago_inicial": {
                required: true,
                number: true,
                min:0.01,
            }
        },
        messages: {
            "cliente": {
                required: "Seleccione al cliente"
            },
            "pago_inicial": {
                required: "Debe ingresar el pago inicial",
                number: "Solo se permiten valores numéricos",
                min:"El valor debe ser mayor de $0",
            },
            "tipo_pago": {
                required: "Selecciona el tipo de pago"
            }
        },
        errorPlacement: function(error, element) {
            if (element.hasClass('select2-hidden-accessible')) {
                error.addClass("invalid-feedback");
                error.insertAfter(element.next('.select2'));
            }
            else if (element.parent().hasClass('input-group')) {
                error.addClass("invalid-feedback");
                error.insertAfter(element.parent());
            } else {
                error.addClass("invalid-feedback");
                error.insertAfter(element);
            }
        },
        highlight: function(element) {
            $(element).addClass("is-invalid");
        },
        unhighlight: function(element) {
            $(element).removeClass("is-invalid");
        }
    });

    // 🔥 Este es el fix para Select2
    $('#cliente, #tipo_pago').on('change.select2', function() {
        $(this).valid();
    });
});
