$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: (data) => {
      $.each(data.results, (index, obj) => {
        $('UL#list_movies').append(`<li>${obj.title}</li>`);
      });
    }
  });
});
