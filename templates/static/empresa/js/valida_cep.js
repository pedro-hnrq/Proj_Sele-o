function preencherEndereco() {
    const cep = document.querySelector('#cep').value;
    if (cep.length === 8) {
      const url = `https://viacep.com.br/ws/${cep}/json/`;
      fetch(url)
        .then(response => response.json())
        .then(endereco => {
          document.querySelector('#logradouro').value = endereco.logradouro;
          document.querySelector('#bairro').value = endereco.bairro;
          document.querySelector('#cidade').value = endereco.localidade;
          document.querySelector('#estado').value = endereco.uf;
        })
        .catch(error => console.log(error));
    }
  }
  
document.querySelector('#cep').addEventListener('keyup', preencherEndereco);