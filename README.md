# RepoGraph 

[![license](https://img.shields.io/github/license/Astro-ton618/repograph.svg)](https://github.com/Astro-ton618/repograph/blob/master/LICENSE)

RepoGraph is a tool that help you visualize the history of a repository by the graph of it's branches.

## Installation

Download this repository.
```zsh
git clone https://github.com/Astro-ton618/repograph.git
```

## Usage

Inside the Repograph folder, build and start the docker.
```zsh
docker build -t repograph .
docker run -dp 5000:5000 repograph
```

## Usage through docker-compose
The other way of starting this application is with docker compose file.
First of all ensure you have install docker compose in your system so that 
you can start this application with single command everytime. Don't worry Installing Docker compose take few mins just visit offical website and it is one time step only.

after that to run this application in dockerized environment run this command
```zsh
docker-compose up  --> to run
docker-compose down --> to stop
``` 

Go tho the default flask [endpoint](http://127.0.0.1:5000/) and paste in the url of the repository.

Enjoy😊

## Contributing

Pull requests are welcome, for major changes, please open an issue first to discuss what you would like to change.

## Authors and acknowledgment

This readme was made using the tool of [makeareadme.com](https://www.makeareadme.com), and [shield.io](https://shields.io).

## License

[MIT](https://choosealicense.com/licenses/mit/)