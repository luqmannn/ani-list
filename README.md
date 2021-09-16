# ani-list
> Thank you to [ShaqeelAhmad](https://github.com/ShaqeelAhmad) for patch to fix slow:turtle: speed by caching it instead of using curl everytime.

A simple shell script (bash) to check weekly most popular anime sorted by views.

The script scrape from [hi10anime](https://hi10anime.com/)

## Dependencies
- awk
- [pup](https://github.com/ericchiang/pup)
- sed
- curl

## Usage
Clone the repo 
- `git clone https://github.com/luqmannn/ani-list.git`

Put the script on one of the PATH environment variable. In this case `/usr/local/bin`
- `sudo cp anlist /usr/local/bin`

To print current PATH environment variable.
- `echo $PATH | tr : \\n`

Don't forget to make the script executable.
- `sudo chmod +x /usr/local/bin/anlist`

## Screenshot
![ani-list-demo](https://raw.githubusercontent.com/luqmannn/ani-list/main/screenshot.png)
