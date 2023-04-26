#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const object = JSON.parse(body);
  const arr = [];
  const dict = {};
  for (const obj of object) {
    if (!(obj.userId in arr)) {
      arr.push(obj.userId);
    }
  }

  for (const item of arr) {
    let count = 0;
    for (const obj of object) {
      if (item === obj.userId && obj.completed === true) {
        count++;
        dict[`${item}`] = count;
      }
    }
  }

  console.log(dict);
});
