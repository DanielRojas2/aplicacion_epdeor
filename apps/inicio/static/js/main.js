var $ = jQuery.noConflict();

function abrir_modal_edicion(url) {
    $('#edicion').load(url, function() {
        $(this).modal('show');
    });
}
function cerrar_modal_edicion() {
    $('#edicion').modal('hide');
}

function abrir_modal_creacion(url) {
    $('#creacion').load(url, function() {
        var modal = new bootstrap.Modal(document.getElementById('creacion'));
        modal.show();
    });
}

function cerrar_modal_creacion() {
    var modal = bootstrap.Modal.getInstance(document.getElementById('creacion'));
    modal.hide();
}
