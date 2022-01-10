![GitHub](https://img.shields.io/github/license/MatrixEternal/rss-reader-cli?style=flat-square)
![GitHub](https://img.shields.io/github/v/release/MatrixEternal/rss-reader-cli?style=flat-square)
![GitHub](https://img.shields.io/github/last-commit/MatrixEternal/rss-reader-cli/main?style=flat-square)

# rss-reader-cli

This RSS feed reader requires setting a feed URL in an ini file and setting up a cron job or Windows Task Scheduler(or other methods).
It will output the posts to a user-specified log file which needs to be constantly read with e.g ``` tail -f ./rss-reader-cli.log```.

## Dependencies:

- python3.8
- configparser
- feedparser

## Steps:

- Clone the repository into your machine
- copy ``` config.ini.example ``` into ``` config.ini ``` and fill it out
- copy ``` cron.example ``` into ``` cron ``` or just copy the expression into your cron tab
  - adjust the paths inside the cron expression

## License

[GPLv3](LICENSE.txt)
