const url =
  "https://api.thingspeak.com/channels/3100740/feeds.json?api_key=50IUUWC8T94XGJS6&";

google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(fetchAndDraw);

function fetchAndDraw() {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      const feeds = data.feeds;

      const temperatures = feeds.map((feed) => ({
        time: feed.created_at,
        temperature: parseFloat(feed.field1),
      }));

      const dataTable = new google.visualization.DataTable();
      dataTable.addColumn("datetime", "Time");
      dataTable.addColumn("number", "Temperature");

      const rows = temperatures
        .map((t) => {
          const d = new Date(t.time);
          if (isNaN(t.temperature) || isNaN(d.getTime())) return null;
          return [d, t.temperature];
        })
        .filter(Boolean)
        .sort((a, b) => a[0] - b[0]);

      if (rows.length === 0) return;

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
}
