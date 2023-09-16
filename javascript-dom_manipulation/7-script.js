fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movie => {
      const ul = document.getElementById('list_movies');
      const li = document.createElement('li');
      li.textContent = movie.title;
      ul.appendChild(li);
    });
  });
