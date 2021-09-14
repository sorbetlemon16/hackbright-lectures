"use strict";

// link.parentElement.parentElement

$('a.view-code').on('click', e => {
  e.preventDefault();

  const rawHtml = $(e.target.parentElement.parentElement)[0]
    .outerHTML
    .split('/n')
    .map(s => s.trim())
  ;

  let indent = -2;
  for (const htmlLine of rawHtml) {
    if 
    $('#viewHtml').append($('<code/>').text(htmlLine).html());
  }



  $('#viewHtml').show();
});
