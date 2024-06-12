import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 7 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  return await getAsync(`item.${itemId}`);
}

app.get('/list_products', (req, res) => {
  const response = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(response);
});


app.get('/list_products/:itemId', async (req, res) => {
  const id = parseInt(req.params.itemId);
  const product = getItemById(id);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  const reservedStock = await getCurrentReservedStockById(id);
  const currentQuantity = product.stock - (reservedStock ? parseInt(reservedStock) : 0);
  res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const id = parseInt(req.params.itemId);
  const product = getItemById(id);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  const reservedStock = await getCurrentReservedStockById(id);
  const currentQuantity = product.stock - (reservedStock ? parseInt(reservedStock) : 0);
  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: id });
  }
  await reserveStockById(id, reservedStock ? parseInt(reservedStock) + 1 : 1);
  res.json({ status: 'Reservation confirmed', itemId: id });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
