function mostrarNomeArquivo() {
    const arquivo = document.getElementById('img').value;
    const nomeArquivo = arquivo.split('\\').pop(); // extrai apenas o nome do arquivo
    document.getElementById('nome-arquivo').textContent = nomeArquivo;
  }