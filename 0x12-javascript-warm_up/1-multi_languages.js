#!/usr/bin/node

const langs = ['C', 'Python', 'JavaScript'];
const adjs = ['fun', 'cool', 'amazing'];

for (let i = 0; i < langs.length && i < adjs.length; i++) {
  console.log(langs[i] + ' is ' + adjs[i]);
}
