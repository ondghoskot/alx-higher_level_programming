#!/usr/bin/node

const langs = ['C', 'Python', 'JavaScript'];
const adjs = ['fun', 'cool', 'amazing'];

for (let i = 0; i < langs.length && i < adjs.length; i++) {
  let lang = langs[i];
  let adj = adjs[i];
  console.log(`${lang} is ${adj}`);
}
