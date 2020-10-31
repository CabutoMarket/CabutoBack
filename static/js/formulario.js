$("#limpiarCampos-btn").click(function() {
	limpiarCampos()
})
$("#guardar-btn").click(function() {
	if (verificarCampos()) {
		$("#form").submit()
	}
})

function limpiarCampos() {
	var inputs = $(".input")
	//LIMPIANDO INPUTS
	inputs.each(function() {
		$(this).val("")
	})
}

function verificarCampos() {
	var verificacion = true
	var inputs = $(".input")
	//VERIFICANDO CADA CAMPO
	inputs.each(function() {if ($(this).val() == "") {verificacion = false}})

	//DISPARANDO ALERTA SI ES NECESARIA
	if (! verificacion) {alert("Por favor llene todos los campos.")}
	return verificacion
}

$(document).on("click", ".btn-modal", function (e) {
    e.preventDefault();
    var $popup = $("#popup");
    var popup_url = $(this).data("popup-url");
    $(".modal-body", $popup).load(popup_url, function () {
      $popup.modal("show");
    });
  });