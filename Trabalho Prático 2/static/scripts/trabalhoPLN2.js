document.addEventListener('DOMContentLoaded', function() {
    const option1 = document.getElementById('esqueleto');
    const option1_v1 = document.getElementById('muscular');
    const option2Container = document.getElementById('option2Container');
    const option3Container = document.getElementById('option3Container');

    option1.addEventListener('change', function() {
        if (option1.checked) {
            option2Container.style.display = 'block';
            option3Container.style.display = 'none'; // Mostra o segundo botão de rádio
            
        } else {
            option2Container.style.display = 'none'; // Oculta o segundo botão de rádio
        }
    });

    option1_v1.addEventListener('change', function() {
        if (option1_v1.checked) {
            option3Container.style.display = 'block';
            option2Container.style.display = 'none'; // Mostra o segundo botão de rádio
            
        } else {
            option3Container.style.display = 'none'; // Oculta o segundo botão de rádio
        }
    });
});

radioForm.addEventListener('submit', function() {
    const selectedOption = document.querySelector('input[name="option_esq"]:checked') 
    if (selectedOption) {
        selectedLabel.value = selectedOption.parentElement.textContent.trim();
    }
});