let opDia = document.getElementById("opDia");
let totales = document.querySelector("[data-id='opTotales']");
let inp = document.getElementById("fechaConsulta");

let opTotales = document.getElementById("opTotales");
let radio = opTotales.querySelectorAll('input[type="radio"]');

let mes = document.getElementById("mes");
let mesSelect = mes.querySelector("select");
let dia = document.getElementById("dia");
let diaSelect = mes.querySelector("select");
opDia.checked = true;

window.onload = inicializar;

function showOpFechas() {
  if (!opDia.checked && totales.style.display == "none") {
    totales.style.display = "block";
    inp.style.display = "none";
    showAdInput();
  } else {
    totales.style.display = "none";
    inp.style.display = "block";
    mes.style.display = "none";
    dia.style.display = "none";
  }
}
function showAdInput() {
  let valueSelected;
  radio.forEach((item) => {
    if (item.checked) {
      valueSelected = item.value;
    }
  });
  if (valueSelected == 1) {
    mes.style.display = "none";
    dia.style.display = "block";
    mesSelect.addEventListener("change", (e) => {
      console.log(e.target.value);
    });
  } else if (valueSelected == 2) {
    mes.style.display = "block";
    dia.style.display = "none";
    diaSelect.addEventListener("change", (e) => {
      console.log(e.target.value);
    });
  }
}

document.addEventListener("DOMContentLoaded", function () {
  var checkboxes = document.querySelectorAll(
    'input[type="radio"][name="ordenes_seleccionadas"]'
  );
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", function () {
      var tr = this.closest("tr");
      if (this.checked) {
        tr.classList.add("fila-orden-checked");
      } else {
        tr.classList.remove("fila-orden-checked");
      }

      var radioGroupName = this.getAttribute("name");
      document.querySelectorAll('input[type="radio"][name="' + radioGroupName + '"]')
      .forEach(otherRadioButton => {
        if (otherRadioButton !== this) {
          var otherTr = otherRadioButton.closest("tr");
          otherTr.classList.remove("fila-orden-checked");
        }
      });
    });
  });

  
});

function inicializar(){  
  document.getElementById("terminar").addEventListener("click", function (e) {
    document.getElementById("formSent").submit();     
  });
  let text = document.getElementsByClassName("modal-body")[0];
  if (text) {
    let message = text.textContent.replace(/\s+/g, ' ').trim();
    console.log(message);
    if (message.includes("confirmar") || message.includes("Selecciona")) {
      if (message.includes("Selecciona")) {
        document.getElementById("modificar").style.display = "none"
      } else {
        document.getElementById("modificar").style.display = "block"
      }

      var myModal = new bootstrap.Modal(document.getElementById("exampleModal"));
      myModal.show();

      document.getElementById("modificar").addEventListener('click', (e) =>{
        document.getElementById("formSent").submit();
        myModal.hide();
      });
      document.querySelector("[data-dismiss='modal']").addEventListener('click', (e) =>{
        myModal.hide();
      });
      document.getElementById("enviarVenta").addEventListener('click', (e) =>{
        document.getElementById("formSent").submit();
        myModal.hide();
      });
    }
  }
  
}