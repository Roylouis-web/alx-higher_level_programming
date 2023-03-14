#!/usr/bin/node
function rev (num) {
  let str = '';
  while (parseInt(num) > 0) {
    str += parseInt(num % 10);
    num /= 10;
  }

  return parseInt(str);
}

exports.converter = function (base) {
  return function myConverter (num) {
    let str = '';

    if (base === 16) {
      if (num === 10) {
        return 'a';
      } else if (num === 11) {
        return 'b';
      } else if (num === 12) {
        return 'c';
      } else if (num === 13) {
        return 'd';
      } else if (num === 14) {
        return 'e';
      } else if (num === 15) {
        return 'f';
      }
    }

    while (parseInt(num) > 0) {
      str += parseInt(num % 10);
      num /= base;
    }
    return (rev(parseInt(str)));
  };
};
