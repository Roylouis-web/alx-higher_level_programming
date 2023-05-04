$(() => {
  $('INPUT#btn_translate').click(() => {
    const code = $('INPUT#language_code').value();
    $('DIV#hello').empty();
    $.ajax({
      type: 'GET',
      url: `https://fourtonfish.com/hellosalut/?lang=${code}`,
      success: (data) => {
        $('DIV#hello').append(data.hello);
      }
    });
  });
});
