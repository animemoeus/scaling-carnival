const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/profile", (req, res) => {
  res.send(`/profile with ${req.method}`);
});

app.post("/profile", (req, res) => {
  res.send(`/profile with ${req.method}`);
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
