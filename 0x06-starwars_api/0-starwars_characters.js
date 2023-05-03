#!/usr/bin/node
const request = require("request");
const movieID = process.argv[2];

function requestPromise(url) {
  return new Promise((resolve, reject) => {
    request.get(url, {}, (error, response) => {
      if (error) {
        return reject(error);
      }

      if (response.statusCode !== 200) {
        return reject(null);
      }

      resolve(JSON.parse(response.body));
    });
  });
}

async function main() {
  if (movieID) {
    const film = await requestPromise(
      `https://swapi-api.alx-tools.com/api/films/${movieID}`
    );

    if (film) {
      for (const url of film.characters) {
        const person = await requestPromise(url);
        console.log(person.name);
      }
    }
  }
}

main().then(() => {});
