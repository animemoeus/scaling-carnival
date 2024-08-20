const express = require("express");
const app = express();
const port = 3000;

// Middleware to validate the header
app.use((req, res, next) => {
  const userId = req.header("User-id");
  const scope = req.header("Scope");

  if (userId !== "ifabula" || scope !== "user") {
    return res
      .status(401)
      .json({ responseCode: 401, responseMessage: "UNAUTHORIZED" });
  }

  next();
});

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
