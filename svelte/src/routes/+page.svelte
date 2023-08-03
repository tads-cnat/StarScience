<script>
  import axios from "axios";

  // Variáveis para armazenar os dados do novo artigo a ser criado
  let name = "";
  let id = "";

    // Função para enviar a requisição POST quando o formulário for enviado
    async function createCategory() {
    console.log("submetido");
    const data = {
      name: name,
      id: id,
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/starscience/category/",
        data
      );
      console.log("Categoria criada com sucesso:", response.data);
      // Você pode tratar a resposta ou redirecionar o usuário após o sucesso
    } catch (error) {
      console.error("Erro ao criar a Categoria:", error);
      // Você pode tratar o erro ou exibir uma mensagem de erro para o usuário
    }
  }
</script>


<!-- svelte-ignore a11y-missing-attribute -->
<html>
  <head>
    <title>Cadastro de Categoria</title>

    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bootstrap demo</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <h1>Cadastrar Categoria</h1>
    <div class="container">
      <form class="col-md-6" on:submit|preventDefault={createCategory}>

        
          
          <input type="number" id="id" bind:value={id} hidden>


        <div class="form-group">
          <label for="area">Categoria:</label>
          <input type="text" id="area" name="area" class="form-control" bind:value={name} />
        </div>
        <br>
        <div class="form-group">
          <button type="submit" class="btn btn-primary">Cadastrar</button>
        </div>

      </form>
    </div>
  </body>
</html>
