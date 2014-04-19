# XKCD Password Generator API

This is an HTTP API written in Python using the [Bottle framework](http://bottlepy.org/docs/dev/index.html) for generating [XKCD style passwords](http://xkcd.com/936/).

The latest version of the API is hosted [here](http://passgen.apoorv.me).

## Installation
To try out the generator, you can clone this repository and run `python main.py`. This will run Bottle's built-in development server and you can access the API from `http://localhost:8080/GeneratePassword`

For production deployment, refer to the Bottle [documentation page](http://bottlepy.org/docs/dev/deployment.html) on deployment.

## Usage

Call `/GeneratePassword/{Mode}` where `{Mode}` can be either `Capitalize`, `LowerCase` or `UpperCase`.

By default, four word passwords with spaces as separators will be generated.

You can specify the number of words and the separator in the query string as follows:
`/GeneratePassword/{Mode}?words=7&separator=65`

Note that you need to pass in the ASCII value of the separator character.