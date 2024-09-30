let binaryString = `
01001000 01100101 01101100 01101100 01101111 00100000 01010110 01101001 01100100 01110101 00101100 00100000 01011001 01101111 01110101 00100000 01100001 01110010 01100101 00100000 01110100 01101000 01100101 00100000 01101101 01101111 01110011 01110100 00100000 01100001 01101101 01100001 01111010 01101001 01101110 01100111 00100000 01110000 01100101 01110010 01110011 01101111 01101110 00100000 01001001 00100000 01101000 01100001 01110110 01100101 00100000 01100101 01110110 01100101 01110010 00100000 01101011 01101110 01101111 01110111 01101110 00100001 00100000 01011001 01101111 01110101 00100000 01100001 01110010 01100101 00100000 01100001 00100000 01110011 01110100 01100001 01110010 00101110
`;
// let binaryString = `
// 01000001 01010011 01000011 01001001 01001001 00100000 01101001 01110011 00100000 01100001 01101101 01100001 01111010 01101001 01101110 01100111 00100001
// `;
let binarySplit = binaryString.trim().split(' ');

let displayEl = document.getElementById('display');
let preDisplayEl = document.getElementById('pre-display');
let preRenderCheckboxEl = document.getElementById('preRender-checkbox');
let hideByteBinaryCheckboxEl = document.getElementById(
  'hideByteBinary-checkbox'
);
let hideByteDecCheckboxEl = document.getElementById('hideByteDec-checkbox');
let removeByteStylesCheckboxEl = document.getElementById(
  'removeByteStyles-checkbox'
);
let byteTemplateEl = document.getElementById('byte-template');
let asciiFontSelectEl = document.getElementById('ascii-font-select');

let preRender = preRenderCheckboxEl.checked;
let hideByteBinary = hideByteBinaryCheckboxEl.checked;
let hideByteDec = hideByteDecCheckboxEl.checked;
let removeByteStyles = removeByteStylesCheckboxEl.checked;
let ftf = 'inherit';

function render() {
  displayEl.innerHTML = '';
  preDisplayEl.textContent = '';

  if (preRender) {
    preDisplayEl.textContent = binaryString;
    hideByteBinaryCheckboxEl.disabled = true;
    hideByteDecCheckboxEl.disabled = true;
    removeByteStylesCheckboxEl.disabled = true;
  } else {
    hideByteBinaryCheckboxEl.disabled = false;
    hideByteDecCheckboxEl.disabled = false;
    removeByteStylesCheckboxEl.disabled = false;

    binarySplit.forEach(str => {
      clone = byteTemplateEl.content.cloneNode(true);

      clone.querySelector('.byte-binary').textContent = str;

      let byteDec = parseInt(str, 2);
      let byteAscii = String.fromCharCode(byteDec);
      byteAscii = byteAscii === ' ' ? '&nbsp;' : byteAscii;
      clone.querySelector('.byte-ascii').innerHTML = byteAscii;
      clone.querySelector('.byte-dec').innerHTML = String(byteDec).padStart(
        3,
        '0'
      );

      displayEl.appendChild(clone);
    });
  }

  toggleHideByteBinary();
  doRemoveByteStyles();
  doAsciiFontSelect();
  toggleHideByteDec();

  // document.querySelectorAll('.byte-binary').forEach(element => {
  //   element.style.display = 'none';
  // });

  // document.querySelectorAll('.byte-ascii').forEach(element => {
  //   element.style.display = 'none';
  // });
}

function toggleHideByteBinary() {
  document.querySelectorAll('.byte-binary').forEach(el => {
    if (hideByteBinary) {
      el.classList.add('hidden');
    } else {
      el.classList.remove('hidden');
    }
  });
}

function toggleHideByteDec() {
  document.querySelectorAll('.byte-dec').forEach(el => {
    if (hideByteDec) {
      el.classList.add('hidden');
    } else {
      el.classList.remove('hidden');
    }
  });
}

function doRemoveByteStyles() {
  document.querySelectorAll('.byte').forEach(el => {
    if (removeByteStyles) {
      el.classList.remove('byte');
    } else {
      el.classList.add('byte');
    }
  });
}

function doAsciiFontSelect() {
  document.querySelectorAll('.byte-ascii').forEach(el => {
    el.style.fontFamily = ftf;
  });
}

render();

preRenderCheckboxEl.addEventListener('change', e => {
  preRender = e.target.checked;
  render();
});

hideByteBinaryCheckboxEl.addEventListener('change', e => {
  hideByteBinary = e.target.checked;
  render();
});

hideByteDecCheckboxEl.addEventListener('change', e => {
  hideByteDec = e.target.checked;
  render();
});

removeByteStylesCheckboxEl.addEventListener('change', e => {
  removeByteStyles = e.target.checked;
  render();
});

asciiFontSelectEl.addEventListener('change', e => {
  ftf = e.target.value;
  render();
});
