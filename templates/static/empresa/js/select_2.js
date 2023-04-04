$(document).ready(function() {
    $('#id_tecnologias').select2({
        templateResult: formatOption
    });
    $('#id_profissao').select2({
        templateResult: formatOption
    });
});

function formatOption(option) {
    if (!option.id) { return option.text; }
    var imgSrc = $(option.element).data('img-src');
    var $option = $(
        '<span><img src="' + imgSrc + '" width="30" height="30"> ' + option.text + '</span>'
    );
    return $option;
}
