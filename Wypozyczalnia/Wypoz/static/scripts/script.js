
$(document).ready( function(){

  $(".car").click(function(){
      $('#details_basic').html('<p> Marka:' + $(this).attr('data-marka') + '</br>model: ' +  $(this).attr('data-model') +'</br>klasa: ' +  $(this).attr('data-klasa') + '</br>kolor: '+  $(this).attr('data-kolor') + '</p></br>');
      $('#details_advanced').html('<p>Wyposazenie: ' +  $(this).attr('data-wypos') + '</br>silnik: ' +  $(this).attr('data-silnik') +'</br>liczba siedzien: ' +  $(this).attr('data-licz_siedz') + '</p>');
      if($(this).hasClass("selected"))
      {
        $(this).removeClass("selected");
      } else {
        $('li').removeClass("selected");
        $(this).addClass("selected");
      }
  });

});



