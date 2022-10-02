const notificacionSwal=(titletext,text,icon,confirmButtonText) => {
    swal.fire({
        titletext: titletext,
        text:text,
        icon:icon, //warning,error,success,info
        confirmButtonText: confirmButtonText,
    });
}

//__________________________________________________________________________________________//
//boton para mensaje de confirmacion

const borrar = document.getElementById('borrar');
//const btnSuccess = document.querySelector('#btnSuccess'); 
// (se podra recorrer con for o pasar varios parametros averiguar como)

borrar.addEventListener('click',function(e) {
            e.preventDefault();
            swal.fire({
                title:" ¿Confirma la solicitud?",
                showCancelButton: true,
                confirmButtonText:"Enviar",
                confirmButtonColor: "green",
                backdrop: true,
                showLoaderOnConfirm: true,
                closeOnConfirm: false,
                preConfirm:() => {


                },
                allowOutsideClick:() => false
                
            }).then(function(isConfirm)
            {                
                if (isConfirm.isConfirmed==true){
                    swal.fire({
                        title:"Lamentamos tu desicion, te vamos a extrañar, recibiras un mail de confirmacion con la eliminacion de tu perfil.",
                        showCancelButton: false,
                        confirmButtonText:"OK",
                        confirmButtonColor: "green",
                        backdrop: false,
                        showLoaderOnConfirm: false,
                        icon: "success",
                        preConfirm:() => {
        
        
                        },
                        allowOutsideClick:() => false
                        
                    })                    
                }
                
            }); 
        });
    