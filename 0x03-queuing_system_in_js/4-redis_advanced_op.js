import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const setHash = (hashName, Name, fieldValues) => {
  client.hset(hashName, Name, fieldValues, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
};

const displayHash = (hashName) => {
  client.hgetall(hashName, (error, reply) => { console.log(reply); });
};

const hashValues = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

Object.entries(hashValues).forEach(([field, value]) => {
  setHash('HolbertonSchools', field, value);
});

displayHash('HolbertonSchools');
