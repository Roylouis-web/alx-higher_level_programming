#!/usr/bin/node
/**
 * a function that returns the reversed version of a list
 */

exports.esrever = function (list) {
  let j = list.length - 1;

  for (let i = 0; i < list.length; i++) {
    if (i < j) {
      [list[i], list[j]] = [list[j], list[i]];
    }
    j--;
  }

  return list;
};
