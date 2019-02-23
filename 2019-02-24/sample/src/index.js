'use strict';

document.addEventListener('DOMContentLoaded', () => {
  const $hello = document.querySelector('#hello');
  $hello.addEventListener('click', () => {
    changeText($hello, 'Hello Abe!');
  });
});
