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

const bttSuccess = document.getElementById('bttSuccess');
//const btnSuccess = document.querySelector('#btnSuccess'); 

bttSuccess.addEventListener('click',function(e) {
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
                        title:"Prcesando, pronto recibiras noticias con el estado de tu solicitud!",
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