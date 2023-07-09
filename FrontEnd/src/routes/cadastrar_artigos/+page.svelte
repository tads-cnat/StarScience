<!DOCTYPE html>
<!-- svelte-ignore a11y-missing-attribute -->
<html>
<head>
  <title>Cadastro de Artigos</title> 
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
    }
    
    .container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
      background-color: #fff;
      border-radius: 5px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    
    .container h2 {
      text-align: center;
    }
    
    .form-group {
      margin-bottom: 20px;
    }
    
    .form-group label {
      display: block;
      font-weight: bold;
      margin-bottom: 5px;
    }
    
    .form-group input[type="text"],
    .form-group input[type="email"],
    .form-group textarea {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
    }
    
    .form-group textarea {
      resize: vertical;
      height: 150px;
    }
    
    .form-group button {
      background-color: #4CAF50;
      color: #fff;
      padding: 10px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      float: right;
    }
    
    .form-group button:hover {
      background-color: #45a049;
    }

    body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
}

.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.container h2 {
  text-align: center;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #333;
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  font-family: Arial, sans-serif;
  color: #333;
}

.form-group textarea {
  resize: vertical;
  height: 150px;
}

.form-group button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  float: right;
  font-family: Arial, sans-serif;
}

.form-group button:hover {
  background-color: #45a049;
}
</style>
</head>
<body>
  
  <div class="container">
    <h2>Formulário de Cadastro de Artigos Científicos</h2>
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
        <button type="submit">Enviar</button>
      </div>
    </form>
  </div>
</body>
</html>

