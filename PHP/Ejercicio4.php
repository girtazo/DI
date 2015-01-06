<?php

  if(!isset($_REQUEST["btnEnviar"])){

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Convertidor de segundos a horas, minutos y segundos (Formulario). Operaciones aritméticas. Ejercicios. PHP. Bartolomé Sintes Marco</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="generator" content="amaya 8.7.1, see http://www.w3.org/Amaya/">
    <link href="hoja4.css" rel="stylesheet" type="text/css" title="Color">
  </head>

  <body>
    <h1>Convertidor de segundos a horas, minutos y segundos (Formulario)</h1>

    <p>Escriba un número de segundos para convertir a horas, minutos y segundos.</p>

    <form action="Ejercicio4.php" method="post">
      <fieldset>
        <legend>Formulario</legend>

        <table class="borde" cellspacing="5">
          <tbody>
            <tr>
              <td><strong>Segundos:</strong></td>
              <td><input name="segundos" size="8" maxlength="8" type="text"> </td>
            </tr>
          </tbody>
        </table>

        <p class="der">
        <input name="btnEnviar" value="Convertir" type="submit"> 
        <input value="Borrar" name="Reset" type="reset"></p>
      </fieldset>
    </form>
  </body>
</html>
<?php

  } else {

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Convertidor de segundos a horas, minutos y segundos (Resultado). Operaciones aritméticas. Ejercicios. PHP. Bartolomé Sintes Marco</title>
    <link href="hoja4.css" rel="stylesheet" type="text/css" title="Color">
  </head>
  <body>
    <h1>Convertidor de segundos a horas, minutos y segundos (Resultado)</h1>
    <?php

        if( $_REQUEST["segundos"] == "" ){
          
          print("<p class=\"aviso\">No ha escrito el número de segundos.</p>\n");
        
        } else if( ! ((int) $_REQUEST["segundos"] >= 0 &&  is_numeric($_REQUEST["segundos"] ) ) ){
          
          print("<p class=\"aviso\">No ha escrito los segundos como número entero positivo.</p>\n");
        
        } else {

          $horas    = floor( $_REQUEST["segundos"] / 3600 );
          $minutos  = floor( ( $_REQUEST["segundos"] - ( $horas * 3600 ) ) / 60 );
          $segundos = $_REQUEST["segundos"] - ( $horas * 3600 ) - ( $minutos * 60 );
          print("<p>" . $_REQUEST["segundos"] . " segundos son " . $horas . " horas, " . $minutos . " minutos y " . $segundos . " segundos</p>");
        
        }
    
    ?>

    <p><a href="Ejercicio4.php">Volver al formulario.</a></p>

  </body>
</html>
<?php
  }
?>

