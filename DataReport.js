// Criação do elemento iframe
const iframe = document.createElement('iframe');

// Configuração dos atributos do iframe
iframe.title = 'DataTvDisplay';
iframe.width = '1140';
iframe.height = '541.25';
iframe.src = 'https://app.powerbi.com/reportEmbed?reportId=b9935033-257d-42a8-ad72-89f06364840f&autoAuth=true&ctid=378f77cd-a5e5-4296-975f-5f14dd44687f';
iframe.frameBorder = '0';
iframe.allowFullScreen = true;

// Obtém a referência do elemento onde o iframe será exibido
const embedContainer = document.getElementById('embedContainer');

// Adiciona o iframe à div no DOM
embedContainer.appendChild(iframe);
