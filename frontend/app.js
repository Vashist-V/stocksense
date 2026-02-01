async function fetchAnalysis()
{
    const symbol = document.getElementById("symbol").value;
    const market = document.getElementById("market").value;

    const res = await fetch(
        `http://127.0.0.1:5000/api/analysis?symbol=${symbol}&market=${market}`
    );

    const data = await res.json();
    document.getElementById("output").innerText =
        `Signal: ${data.decision.signal}\n` +
        `Confidence: ${data.decision.confidence}\n` +
        `Reason: ${data.decision.reason}`;

}

async function fetchTrending() {
  const market = document.getElementById("market").value;

  const res = await fetch(
    `http://127.0.0.1:5000/api/trending?market=${market}`
  );

  const data = await res.json();

  document.getElementById("output").innerText =
    "Top Gainers:\n" +
    JSON.stringify(data.gainers, null, 2) +
    "\n\nTop Losers:\n" +
    JSON.stringify(data.losers, null, 2);
}

