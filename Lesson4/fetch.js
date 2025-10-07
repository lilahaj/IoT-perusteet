const url =
  "https://api.thingspeak.com/channels/3100740/feeds.json?api_key=50IUUWC8T94XGJS6&";

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    const feeds = data.feeds;

    const temperatures = feeds.map((feed) => ({
      time: feed.created_at,
      temperature: parseFloat(feed.field1),
    }));
    document.getElementById("output").innerText = JSON.stringify(temperatures);
  })

  .catch((error) => {
    console.error("Error fetching data:", error);
    document.getElementById("output").textContent = "Error loading data";
  });
