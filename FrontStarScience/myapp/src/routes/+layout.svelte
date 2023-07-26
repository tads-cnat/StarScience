<script>
  import "../app.postcss";
  import Header from "$lib/Header.svelte";
  import Footer from "$lib/Footer.svelte";
</script>

<!-- svelte-ignore component-name-lowercase -->
<Header />
<slot />
<!-- svelte-ignore missing-declaration -->
<Footer />


