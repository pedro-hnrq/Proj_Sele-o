function preencherEndereco() {  

  var cepField = document.querySelector("#cep");
  var cep = cepField.value.replace(/\D/g, '');
  
  if (cep.length > 8) {
    cep = cep.slice(0, 8);
  }

  cep = cep.replace(/^(\d{5})(\d)/, "$1-$2");

  cepField.value = cep;

  // const cep = document.querySelector('#cep').value;
  if (cep.length === 9) {
    const url = `https://viacep.com.br/ws/${cep}/json/`;
    fetch(url)
      .then(response => response.json())
      .then(endereco => {
        document.querySelector('#logradouro').value = endereco.logradouro || 'Não existe essa Rua';
        document.querySelector('#bairro').value = endereco.bairro || "Não existe essa Bairro";
        document.querySelector('#cidade').value = endereco.localidade || "Não existe essa Cidade";
        document.querySelector('#estado').value = endereco.uf || "Não existe essa UF";
      })        
  }else {
    // Se o CEP não tiver 8 caracteres, limpa os campos de endereço
    document.getElementById("#logradouro").value = "";
    document.getElementById("#bairro").value = "";
    document.getElementById("#cidade").value = "";
    document.getElementById("#estado").value = "";
  }
  // if (cep.length == 9) {
  //   $.getJSON("https://viacep.com.br/ws/"+cep+"/json/", function(data) {
  //       if (!("erro" in data)) {
  //           // Se o CEP for válido, preenche os campos de endereço
  //           document.getElementById("#logradouro").value = data.logradouro;
  //           document.getElementById("#bairro").value = data.bairro;
  //           document.getElementById("#cidade").value = data.localidade;
  //           document.getElementById("#estado").value = data.uf;
  //       }
  //       else{
  //         // Se o CEP for inválido ou não encontrado, exibe uma mensagem de erro
  //           document.getElementById("#logradouro").value = "Não existe essa logradouro";
  //           document.getElementById("#bairro").value = "Não existe essa bairro";
  //           document.getElementById("#cidade").value = "Não existe essa cidade";
  //           document.getElementById("#estado").value = "Não existe essa UF";
  //       }
  //   });
  // }else {
  //   // Se o CEP não tiver 8 caracteres, limpa os campos de endereço
  //   document.getElementById("#logradouro").value = "";
  //   document.getElementById("#bairro").value = "";
  //   document.getElementById("#cidade").value = "";
  //   document.getElementById("#estado").value = "";
  // }
  
}
  
// document.querySelector('#cep').addEventListener('keyup', preencherEndereco);