#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const len = list.length;
  let Orc = 0;
  let i = 0;

  for (i = 0; i < len; i++) {
    if (list[i] === searchElement) {
      Orc++;
    }
  }
  return Orc;
};
