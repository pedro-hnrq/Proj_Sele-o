function preencherEndereco() {  

  var cepField = document.querySelector("#cep");
  var cep = cepField.value.replace(/\D/g, '');
  
  if (cep.length > 8) {
    cep = cep.slice(0, 8);
  }

  cep = cep.replace(/^(\d{5})(\d)/, "$1-$2");

  cepField.value = cep;

  const url = `https://viacep.com.br/ws/${cep}/json/`;
  fetch(url)
    .then(response => response.json())
    .then(endereco => {
      if (!endereco.erro) {
        document.querySelector('#logradouro').value = endereco.logradouro || 'Não existe essa Rua';
        document.querySelector('#bairro').value = endereco.bairro || "Não existe esse Bairro";
        document.querySelector('#cidade').value = endereco.localidade || "Não existe essa Cidade";
        document.querySelector('#estado').value = endereco.uf || "Não existe esse Estado";
        const notificacao = document.querySelector('#notificacao-cep');
        if (notificacao) {
          notificacao.remove();
        }
      } else {
        document.querySelector('#logradouro').value = "";
        document.querySelector('#bairro').value = "";
        document.querySelector('#cidade').value = "";
        document.querySelector('#estado').value = "";
        const notificacao = document.createElement('div');
        notificacao.textContent = 'CEP inválido';
        notificacao.style.color = 'red';
        notificacao.setAttribute('id', 'notificacao-cep');
        cepField.parentNode.insertBefore(notificacao, cepField.nextSibling);
        setTimeout(() => {
          notificacao.remove();
        }, 5000);
      }
    })
    .catch(error => {
      console.error('Erro ao consultar CEP:', error);
    });
  
}
  
// document.querySelector('#cep').addEventListener('keyup', preencherEndereco);