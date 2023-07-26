<script>
    import ButtonEnv from "$lib/ButtonEnv.svelte";
    import Footer from "$lib/Footer.svelte";
    import Menu from "$lib/Menu.svelte";
</script>

<!DOCTYPE html>
<!-- svelte-ignore a11y-missing-attribute -->
<html>
<head>
  <title>Cadastro de Artigos</title> 
</head>
<body>
  <h1>Cadastrar Artigos</h1>
  <div class="container">
    <form>
      <div class="form-group">
        <label for="titulo">Título do Artigo:</label>
        <input type="text" id="titulo" name="titulo" required>
      </div>
      <div class="form-group">
        <label for="autor">Autor(es):</label>
        <input type="text" id="autor" name="autor" required>
      </div>
      <div class="form-group">
        <label for="email">E-mail:</label>
        <input type="email" id="email" name="email" required>
      </div>
      <div class="form-group">
        <label for="DOI">DOI:</label>
        <input type="text" id="DOI" name="DOI" required>
      </div>
      <div class="form-group">
        <label for="INSS">INSS:</label>
        <input type="text" id="INSS" name="INSS" required>
      </div>
      <div class="form-group">
        <label for="periodigo">Periódigo:</label>
        <input type="text" id="periodigo" name="periodigo" required>
      </div>
      <div class="form-group">
        <label for="area">Área:</label>
        <input type="text" id="area" name="area" required>
      </div> 
      <div class="form-group">
        <label for="periodigo">Periódigo:</label>
        <input type="text" id="periodigo" name="periodigo" required>
      </div>  
      <div class="form-group">
        <label for="resumo">Resumo:</label>
        <textarea id="resumo" name="resumo" required></textarea>
      </div>
      <div>
        <label for="artigo">Selecione o artigo:</label>
        <input type="file" id="artigo" name="artigo">
      </div>
      <div class="form-group">
        <ButtonEnv />
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
  align: center;
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

input[type="text"],
input[type="email"],
textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 20px;
  border: 1px solid rgb(255, 255, 255)fff;
  border-radius: 10px;
}

/* Estilos para campos requeridos (HTML5) */
input:required,
textarea:required {
  border-color: #4d4d4d;
}

</style>

