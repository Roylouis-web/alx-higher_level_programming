#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const args = process.argv;
const fileA = args[2];
const fileB = args[3];
const fileC = args[4];
const message1 = fs.readFileSync(fileA).toString();
const message2 = fs.readFileSync(fileB).toString();
fs.writeFileSync(fileC, message1 + message2);
