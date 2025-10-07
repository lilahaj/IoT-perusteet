const url =
  "https://api.thingspeak.com/channels/3100740/feeds.json?api_key=50IUUWC8T94XGJS6&results=100";

google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(fetchAndDraw);

function fetchAndDraw() {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const feeds = data.feeds || [];

      const dataTable = new google.visualization.DataTable();
      dataTable.addColumn("datetime", "Time");
      dataTable.addColumn("number", "Temperature");

      const rows = feeds
        .map((feed) => {
          const t = parseFloat(feed.field1);
          const time = new Date(feed.created_at);
          if (isNaN(t) || isNaN(time.getTime())) return null;
          return [time, t];
        })
        .filter(Boolean);

      if (rows.length === 0) {
        document.getElementById("output").innerText = "No valid data";
        return;
      }
      rows.sort((a, b) => a[0] - b[0]);

      dataTable.addRows(rows);

      const options = {
        title: "Temperature",
        height: 400,
        hAxis: { title: "Time", format: "HH:mm:ss" },
        vAxis: { title: "°C" },
        legend: { position: "none" },
      };

      const chart = new google.visualization.LineChart(
        document.getElementById("chart_div")
      );
      chart.draw(dataTable, options);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
      document.getElementById("output").textContent = "Error loading data";
    });

  setTimeout(fetchAndDraw, 60000);
}
