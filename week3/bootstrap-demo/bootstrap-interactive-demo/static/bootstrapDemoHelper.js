const columnElements = document.querySelectorAll('div.col');

for (const element of columnElements) {
  const color = randomColor({format: 'hsl'});
  element.style.backgroundColor = color;
  if (Number(color.split(',')[2].trim().replace('%)', '')) < 45) {
    element.style.color = 'white';
    element.classList.add('dark');
  }
}
