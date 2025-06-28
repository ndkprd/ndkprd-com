# ndkprd.com

A dead simple personal site.

## Want to make this yours?

### Using Github Actions

1. Use this repo as a template;
2. Update the configurations inside of `./config.yaml` file;
3. Push the repository into your github account.

At this point, the Github Actions should run and template the web into the `./output` directory on a new branch called `production`. You can configure your hosting provider (or your own automation setup) to sync and publish web inside of that directory. 

### Manually

1. Clone this repo;
2. Update the configurations inside of `config.yaml`file;
3. Run the `MAKE.py` file. It will then generate a static web inside of `./output` directory;
4. Serve this file on your preferred provider or webserver. 

## License

[MIT](./LICENSE)
