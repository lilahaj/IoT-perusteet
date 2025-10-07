import express from "express";

const app = express();
const port = 3000;

const DISCORD_WEBHOOK_URL =
  "https://discord.com/api/webhooks/1425166983502233701/siZhfdsCIDc4z1JBd506BfA2ACgJkt3biyL3yMjIUlWxJ3OP8pqtgmTu2n0eLUvp6aGk";

app.use(express.json());

app.post("/notify", (req, res) => {
  const { message } = req.body;

  if (!message) {
    return res.status(400).json({ error: "Message is required" });
  }
  fetch(DISCORD_WEBHOOK_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ content: message }),
  }).then((response) => {
    if (!response.ok) {
      throw new Error(`Discord responded with status ${response.status}`);
    }
    res.json({ status: "Message sent" });
  })
  .catch((error) => {
    console.error("Error sending message to Discord:", error);
    res.status(500).json({ error: "Failed to send message" });
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
