function initQuagga() {
  const resultElement = document.getElementById('result');
  
  Quagga.init({
    inputStream : {
      name : "Live",
      type : "LiveStream",
      constraints: {
        width: {min: 640},
        height: {min: 480},
        aspectRatio: {min: 1, max: 100},
        facingMode: "environment" // Use la cámara trasera si está disponible
      }
    },
    decoder : {
      readers : ["ean_reader"] // Use el lector de códigos EAN-13
    }
  }, function(err) {
      if (err) {
          console.log(err);
          resultElement.innerHTML = `<p>Error al iniciar Quagga: ${err}</p>`;
          return
      }
      console.log("Iniciando Quagga...");
      Quagga.start();
  });

  Quagga.onDetected(function(result) {
    console.log(result);
    resultElement.innerHTML = `<p>Código de barras detectado: ${result.codeResult.code}</p>`;
  });
}

window.onload = function() {
  initQuagga();
};
