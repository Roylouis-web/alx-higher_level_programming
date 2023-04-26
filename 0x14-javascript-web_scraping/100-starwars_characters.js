const request = require('request');
const process = require('process');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const object = JSON.parse(body);
    for (const url2 of object.characters) {
      request(url2, (error2, response2, body2) => {
        if (error2) {
          console.log(error2);
        } else {
          const object2 = JSON.parse(body2);
          console.log(object2.name);
        }
      });
    }
  }
});
