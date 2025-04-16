const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = 5000;

app.use(bodyParser.json());

app.post('/api', (req, res) => {
  const name = req.body.name;
  res.json({ message: `Hello, ${name} from Express backend!` });
});

app.listen(PORT, () => {
  console.log(`Backend running on port ${PORT}`);
});
