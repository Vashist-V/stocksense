async function fetchPrice() {
  const symbol = document.getElementById("symbol").value;
  const market = document.getElementById("market").value;

  const res = await fetch(
    `http://127.0.0.1:5000/api/price?symbol=${symbol}&market=${market}`
  );

  const data = await res.json();
  document.getElementById("output").innerText = JSON.stringify(data);
}
