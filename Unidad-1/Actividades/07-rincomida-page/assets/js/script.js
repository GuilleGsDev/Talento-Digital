$(document).ready(function() {

    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

    $('#enviarCorreo').click(function() {
        alert("El correo fue enviado correctamente...");
    });

    $('h4').on('dblclick', function() {
        $(this).css("color", "#DC3545"); 

    $('.card-title-toggle').click(function() {
        $('.card-text').toggle(); 
    });

});