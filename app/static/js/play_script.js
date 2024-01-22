$(document).ready(function(){
    function createSpan(text, idContainer){
        let container = $('#' + idContainer);
        for (let i = 0; i < text.length; i++) {
            const span = $('<span></span>');
            span.text(text[i]);
            container.append(span);
        }    
    }
    
    function removeSpans(idContainer) {
        let container = $('#' + idContainer);
        container.empty();
    }

    function createText(nLine){
        if(nLine == endLine){
            var currentText = textHiden[nLine];
            removeSpans('current-word')
            createSpan(currentText,'current-word');    
        }
        else {
            var currentText = textHiden[nLine];
            var nextText = textHiden[nLine+1];
            removeSpans('current-word')
            createSpan(currentText,'current-word');    
            removeSpans('next-word')
            createSpan(nextText,'next-word')        
        }
    }
    
    function send_infos(game_id,line,currentText,myText,time){
        return new Promise(function(resolve, reject) {
            $.ajax({
                type: 'POST',
                url: '/game/update_text',
                data: JSON.stringify({
                    game_id:game_id,
                    line: line,
                    currentText: currentText,
                    myText: myText,
                    time: time
                }),
                contentType: 'application/json;charset=UTF-8',
                success: function(response) {
                    resolve(response)
                },
                error: function(error) {
                    // Rejeita a Promise em caso de erro
                    reject(error);
                }
            })
        })
    }

    const textHiden = String($('#texto_de_aprendizado').text()).split('\n');
    for (var i = 0; i < textHiden.length; i++) {
        textHiden[i] = textHiden[i].trimStart();
    }

    
    const url = String(window.location.href);
    const index = url.search(/\/(?!.*\/)/);
    const infos = url.substring(index+1).split('-');
    const game_id = infos[1];
    
    var lastNewText = '';
    
    var currentLine = -1;
    var endLine = textHiden.length-1;
    send_infos(game_id,currentLine,null,null,Date.now()).then(function(response) {
        currentLine = response.line;
        createText(currentLine)
    })

       

    $('#inputText').keydown(function(event) {
        if (event.keyCode === 13) {
            let time = Date.now();
            send_infos(game_id,currentLine,textHiden[currentLine],$(this).val(),time).then(function(response) {
        currentLine = response.line
    })
            $(this).val('');
            currentLine += 1;
            createText(currentLine)
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