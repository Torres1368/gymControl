
$(document).ready(function() {
    $("#frm_cliente").validate({
        rules: {
  
            "nombre": {
                required: true,
                minlength: 3,
                maxlength: 30,
                lettersonly: true
                
            },
            "apellido": {
                required: true,
                minlength: 3,
                maxlength: 30,
                lettersonly: true
  
            },
            "genero": {
                required: true,  
            }
        },
        messages: {
  
            "nombre": {
                required: "Debe ingresar el nombre del cliente",
                minlength: "Debe ingresar 3 o más caracteres",
                maxlength: "solo se permite hasta 30 caracteres",
                lettersonly: "Solo se permiten letras"
  
  
            },
            "apellido": {
                required: "Debe ingresar el apellido del cliente",
                minlength: "Debe ingresar 3 o más caracteres",
                maxlength: "solo se permite hasta 30 caracteres",
                lettersonly: "Solo se permiten letras"
  
            },
  
            "genero": {
                required: "Seleccione el género del cliente"
  
            }
        }
    });
  });
  