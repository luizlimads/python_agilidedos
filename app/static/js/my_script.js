// Tenho que dar um get de algum lugar para obter essas inforações
const textLearning = "banana é doce\njaca é pesada\na cor da laranja não é laranja".split("\n");
const idGame = 1;

$(document).ready(function(){
    
    function createSpan(text, idContainer){
        let container = $('#' + idContainer);
        for (let i = 0; i < text.length; i++) {
            const span = $('<span></span>');
            span.text(text[i]);
            container.append(span);
        }    
    }

    var currentText = textLearning[0];
    createSpan(currentText,'current-word');
    
    if(textLearning.length > 1){
        var nextText = textLearning[1];
        createSpan(nextText,'next-word')
    }

    var lastNewText = '';
    var timeStart = Date.now();

    $('#inputText').keydown(function(event) {
        if (event.keyCode === 13) {
            let timeEnd = Date.now();
            $.ajax({
                type: 'POST',
                url: '/game/update_text',
                data: JSON.stringify({
                    currentText: currentText,
                    myText: $(this).val(),
                    idGame: idGame
                }),
                contentType: 'application/json;charset=UTF-8',
                success: function(response) {
                    $('.statics span').eq(1).text(response.time);
                }
            });
            $(this).val('');
        }
    });

    $('#inputText').on('input', function() {
        var newText = String($(this).val());
        let is_erasing = lastNewText.length > newText.length;

        if(is_erasing){
            let spanLast = $('#current-word span').eq(lastNewText.length -1)
            spanLast.removeClass('char-erro');
            spanLast.removeClass('char-sucess');
        } else {
            let lastCharNewText = newText.slice(-1);
            let spanCurrentWord = $('#current-word span').eq(newText.length -1)
            
            if(lastCharNewText == spanCurrentWord.text() ){
                spanCurrentWord.removeClass('char-erro');
                spanCurrentWord.addClass('char-sucess');
            } else {
                spanCurrentWord.removeClass('char-sucess');
                spanCurrentWord.addClass('char-erro');
            }
        }
        lastNewText = newText;
    });

});