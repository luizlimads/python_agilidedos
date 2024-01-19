$(document).ready(function(){
    $('#btn_new_game').click(function(){
        $.ajax({
            type: 'GET',
            url: '/game/get-words',
            success: function(data){
                console.log(data)
                // Atualiza a div 'dados' com os dados recebidos
                $('#dados').html(JSON.stringify(data));
            }
        });
    });
});