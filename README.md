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
```{sh}
git clone https://github.com/luqmannn/ani-list.git
```

Put the script on one of the PATH environment variable. In this case `/usr/local/bin`
```{sh}
sudo cp anlist /usr/local/bin
```

To print current PATH environment variable.
```{sh}
echo $PATH | tr : \\n
```

Don't forget to make the script executable.
```{sh}
sudo chmod +x /usr/local/bin/ani-list
```

## Screenshot
![ani-list-demo](https://raw.githubusercontent.com/luqmannn/ani-list/main/screenshot.png)

> I might as well provide the python version as well or any other language in the near future.
