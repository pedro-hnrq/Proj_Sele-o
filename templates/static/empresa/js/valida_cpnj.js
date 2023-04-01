const inputCNPJ = document.querySelector('#cnpj');

inputCNPJ.addEventListener('input', (event) => {
  let cnpj = event.target.value;

  // Remove tudo que não é número
  cnpj = cnpj.replace(/\D/g, '');

  // Adiciona os pontos, barra e traço
  cnpj = cnpj.replace(/(\d{2})(\d)/, '$1.$2');
  cnpj = cnpj.replace(/(\d{3})(\d)/, '$1.$2');
  cnpj = cnpj.replace(/(\d{3})(\d)/, '$1/$2');
  cnpj = cnpj.replace(/(\d{4})(\d{2})$/, '$1-$2');
  
    // Verifica se o CNPJ é válido
    

    // Muda a cor da borda do input se o CNPJ for inválido
    if (cnpj.length === 18 && /^(\d{2}).(\d{3}).(\d{3})\/(\d{4})-(\d{2})$/.test(cnpj)) {
        event.target.classList.remove('invalid');
    } else {
        event.target.classList.add('invalid');
    }

  event.target.value = cnpj;
});
