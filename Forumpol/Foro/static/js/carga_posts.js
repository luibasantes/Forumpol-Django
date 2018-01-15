$(document).ready(function(){
    $('#myTable').DataTable( {
        "order": [[ 2, "desc" ]],
        "language": {
            "lengthMenu": "Mostrando _MENU_ registros por pagina",
            "zeroRecords": "No pudimos encontrar registros. Lo sentimos",
            "info": "Mostrando pagina  _PAGE_ de _PAGES_",
            "infoEmpty": "No hay registros",
            "infoFiltered": "(filtrado desde _MAX_ el total de registros)",
            "paginate": {
                "first":      "Primero",
                "last":       "Ultimo",
                "next":       "Siguiente",
                "previous":   "Anterior"
            }
        }
    } );
});

