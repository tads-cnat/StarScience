<script>

    import Footer from "$lib/Footer.svelte";
    import Menu from "$lib/Menu.svelte";

</script>
<!DOCTYPE html>
<!-- svelte-ignore a11y-missing-attribute -->
<html>
<head>
<title>Star Science</title>
<link rel="style" href="style">
</head>
<body>
  <h1>Star Science</h1>
  <p>Projeto focado em ser uma rede social simples para debate de artigos científicos.</p>
  <div>
    <h2>Equipe Star Science:</h2>
    <ol>
      <li>Joana Fernandes</li>
      <li>Paulo Henrique</li>
      <li>Tiago Assunção</li>
      <li>Virgínia Menezes</li>
    </ol>
  </div>
  <div>
    <h2>Tecnologias Utilizadas:</h2>
    <p>Djhango Rest Framework, Svelte e SQL</p>
  </div>
  <div class="link">
    <h2>Documentação:</h2>
    <a href="https://github.com/tads-cnat/StarScience/blob/main/doc/documentacao.md#documenta%C3%A7%C3%A3o-do-projeto">Visite a documentação no GitHub!</a>
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

/* Estilo para o título h2 */
h2 {
  font-size: 28px;
  font-weight: normal;
  color: #000000;
  text-align: center;
  margin: 20px 0px 0px 20px;
}
p {
  font-size: 16px;
  line-height: 1.6;
  text-align: center;
  color: rgb(0, 0, 0);
}

ol {
  text-align: center;
}

.link{
  text-align: center;
}

a{
  text-decoration: underline;
}

</style>


