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
        $('#id_car_id').val($(this).attr('data-id'));
      }
  });

  $("#person").click(function(){
    $(this).prop("checked", true);
    $("#company").prop("checked", false);
    $("#fields_s").html('<input class="short" type="text" name="imie" placeholder="Imie" required><input class="short" type="text" name="nazwisko" placeholder="Nazwisko"required><input class="long" type="text" name="ulica" placeholder="Ulica" required> <input class="short" type="text" name="miasto" placeholder="Miasto" required> <input class="short" type="email" name="email" placeholder="Mail" required><input class="long" type="text" name="pesel" placeholder="Pesel" required> <input class="short" type="text" name="telefon" placeholder="Telefon" required> <input class="short" type="text" name="nr_dowodu_osobistego" placeholder="Nr dowodu osobistego" required> <input class="short" type="text" name="login" placeholder="Login" required> <input class="short" type="password" name="haslo" placeholder="Haslo" required>');
  });

  $("#company").click(function(){
    $(this).prop("checked", true);
    $("#person").prop("checked", false);
    $("#fields_s").html(' <input class="short" type="text" name="nazwa" placeholder="Nazwa pelna" required><input class="short" type="text" name="nazwa_skr" placeholder="Nazwa skrocona"required><input class="long" type="text" name="nip" placeholder="NIP" required> <input class="short" type="text" name="regon" placeholder="REGON" required> <input class="short" type="text" name="rodzaj" placeholder="Rodzaj dzialalnosci" required> <input class="long" type="text" name="nr_dowodu_osobistego" placeholder="Numer dowodu" required> <input class="short" type="text" name="imie" placeholder="Imie" required> <input class="short" type="text" name="nazwisko" placeholder="Nazwisko" required> <input class="short" type="text" name="login" placeholder="Login" required> <input class="short" type="password" name="haslo" placeholder="Haslo" required>');
  })

  $("#days").change(function(){
      var cost = parseInt($(this).attr('data-cena')) * parseInt($(this).val());
      $("#cost_final").html(cost);
  });
});



