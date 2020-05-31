const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function()  {
  $('#message').fadeOut('fast')
}, 3000);
