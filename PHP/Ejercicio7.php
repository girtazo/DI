<?php

  if(!isset($_REQUEST["btnEnviar"])){

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Datos personales 7 (Formulario). Controles en formularios. Ejercicios. PHP. Bartolomé Sintes Marco</title>
    <meta name="generator" content="amaya 8.7.1, see http://www.w3.org/Amaya/">
    <link href="hoja7.css" rel="stylesheet" type="text/css" title="Color">
  </head>

  <body>

    <form action="Ejercicio7.php" method="post">
      <h1>Datos personales 7 (Formulario)</h1>
      <fieldset>
        <legend>Formulario</legend>
        <p>Escriba los datos siguientes:</p>

        <table cellspacing="5">
          <tbody>
            <tr>
              <td><strong>Nombre:</strong><br>
                <input type="text" name="nombre" size="20" maxlength="20"></td>
              <td><strong>Apellidos:</strong><br>
                <input type="text" name="apellidos" size="20" maxlength="20"></td>
              <td><strong>Edad:</strong><br>

                <select name="edad">
                  <option selected="selected"></option>
                  <option value="1">Menos de 20 años</option>
                  <option value="2">Entre 20 y 39 años</option>
                  <option value="3">Entre 40 y 59 años</option>
                  <option value="4">60 años o más</option>
                </select>
                 </td>
            </tr>
            <tr>
              <td><strong>Peso:<br>
                </strong><input type="text" name="peso" size="3" maxlength="3">
              kg</td>
              <td><strong>Sexo:</strong><br>
                <input type="radio" name="sexo" value="hombre">Hombre <input type="radio" name="sekso" value="mujer">Mujer</td>
              <td><strong>Estado Civil:</strong><br>
                <input type="radio" name="estadoCivil" value="soltero"> Soltero
                <input type="radio" name="estadoCivil" value="casado"> Casado
                <input type="radio" name="estadoCivil" value="otro"> Otro</td>
            </tr>
          </tbody>
        </table>

        <table cellspacing="5">
          <tbody>
            <tr>
              <td rowspan="2" class="borde"><strong>Aficiones:</strong></td>
              <td><input type="checkbox" name="cine"> Cine</td>
              <td><input type="checkbox" name="literatura"> Literatura</td>
              <td><input type="checkbox" name="tebeos"> Tebeos</td>
            </tr>
            <tr>
              <td><input type="checkbox" name="deporte"> Deporte</td>
              <td><input type="checkbox" name="musica"> Música</td>
              <td><input type="checkbox" name="television"> Televisión</td>
            </tr>
          </tbody>
        </table>

        <p class="der">
        <input type="submit" name="btnEnviar" value="Enviar"> 
        <input type="reset" value="Borrar" name="Reset"></p>
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
    <title>Datos personales 7 (Resultado). Controles en formularios. Ejercicios. PHP. Bartolomé Sintes Marco</title>
    <link href="hoja7.css" rel="stylesheet" type="text/css" title="Color">
  </head>
  <body>
    <h1>Datos personales 7 (Resultado)</h1>
    <?php
        if( $_REQUEST["nombre"] != "" ){
          print("<p>Su nombre es <strong>".$_REQUEST["nombre"]."</strong>.</p>\n");
        } else {
          print("<p class=\"aviso\">No ha escrito su nombre.</p>\n");
        }
        if( $_REQUEST["apellidos"] != "" ){
          print("<p>Sus apellidos son <strong>".$_REQUEST["apellidos"]."</strong>.</p>\n");
        } else {
          print("<p class=\"aviso\">No ha escrito su apellidos.</p>\n");
        }
        if( $_REQUEST["edad"] !="" ){
          switch ($_REQUEST["edad"]) {
            case 1:
              $_REQUEST["edad"] = "Menos de 20 años";
              break;
            case 2:
              $_REQUEST["edad"] = "Entre 20 y 39 años";
              break;
            case 3:
              $_REQUEST["edad"] = "Entre 40 y 59 años";
              break;
            case 4:
              $_REQUEST["edad"] = "60 años o más";
              break;
          }
          print("<p>Tiene <strong>".$_REQUEST["edad"]."</strong>.</p>\n");
        } else {
          print("<p class=\"aviso\">No ha indicado su  edad.</p>\n");
        }
        if( $_REQUEST["peso"] != "" ){
          print("<p>Su peso es de <strong>".$_REQUEST["peso"]."</strong>.</p>\n");
        } else {
          print("<p class=\"aviso\">No ha escrito su peso.</p>\n");
        }
        if( isset($_REQUEST["sexo"]) ){
          print("<p>Es un/a <strong>".$_REQUEST["sexo"]."</strong>.</p>\n");
        } else {
          print("<p class=\"aviso\">No ha seleccionado su sexo.</p>\n");
        }
        if( isset($_REQUEST["estadoCivil"]) ){
          print("<p>Su estado civil es <strong>".$_REQUEST["estadoCivil"]."</strong>.</p>\n");
        } else {
            print("<p class=\"aviso\">No ha marcado su estado civil.</p>\n");
        }
        $aficiones = false;
        if( isset($_REQUEST["cine"]) ){
          $aficiones[] =  "cine";
        }
        if( isset($_REQUEST["deporte"]) ){
          $aficiones[] =  "deporte";
        }
        if( isset($_REQUEST["musica"]) ){
          $aficiones[] =  "musica";
        }
        if( isset($_REQUEST["tebeos"]) ){
          $aficiones[] =  "tebeos";
        }
        if( isset($_REQUEST["literatura"]) ){
          $aficiones[] =  "literatura";
        }
        if( isset($_REQUEST["television"]) ){
          $aficiones[] =  "television";
        }
        if( $aficiones ){
          print("<p>Le gusta: ");
          foreach ($aficiones as $key => $value) {
            print($value.", ");
          }
          print("</p>\n");
        } else {
          print("<p class=\"aviso\">No ha marcado ninguna afición.</p>\n");
        }
    ?>

    <p><a href="Ejercicio7.php">Volver al formulario.</a></p>

  </body>
</html>
<?php
  }
?>

