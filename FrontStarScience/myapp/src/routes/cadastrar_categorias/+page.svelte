<script>
    import ButtonCad from "$lib/ButtonCad.svelte";
    import Footer from "$lib/Footer.svelte";
    import Menu from "$lib/Menu.svelte";
</script>

<!DOCTYPE html>
<!-- svelte-ignore a11y-missing-attribute -->
<html>
<head>
  <title>Cadastro de Categorias</title>
</head>
<body>
  <h1>Cadastrar Categorias</h1>
  <div class="container">
  <form>
    <div class="form-group">
      <label for="categoria">Nome da Categoria:</label>
      <input type="text" id="categoria" name="categoria" required>
    </div>
    <div class="form-group">
      <label for="subcategoria">Nome da Sub-Categoria:</label>
      <input type="text" id="subcategoria" name="subcategoria" required>
    </div>
    <div class="form-group">
      <ButtonCad />
    </div>
  </form>
</div>
</body>
</html>

<style>
    body{
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    background-color: rgb(255, 255, 255);
    margin: 10px 10px 10px 10px;
    padding: 0;
  }
  div{
  margin: 10px 10px 10px 10px;
}

  /* Estilo para o título h1 */
h1 {
  font-size: 36px;
  font-weight: normal;
  color: #000000;
  text-align: center;
  margin: 20px 0px 0px 0px;
}
form {
  max-width: auto;
  margin: 20px auto 0px 350px;
  padding: 20px;
  background-color: #ffffff;
  border: 0.3px solid #ffffff;
  border-radius: 10px;
  box-shadow: 0 0 10px rgb(142, 142, 142);
}

label {
  display: block;
  margin-bottom: 10px;
}

input[type="text"]{
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid rgb(255, 255, 255)fff;
  border-radius: 10px;
}

/* Estilos para campos requeridos (HTML5) */
input:required{
  border-color: #4d4d4d;
}

</style>

