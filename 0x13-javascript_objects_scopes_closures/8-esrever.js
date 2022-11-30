#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length - 1;
  const Orc = [];
  let i = 0;

  for (i = len; i >= 0; i--) {
    Orc.push(list[i]);
  }
  return Orc;
};
