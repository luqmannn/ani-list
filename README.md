# ani-list
> Thank you to [ShaqeelAhmad](https://github.com/ShaqeelAhmad) for patch to fix slow:turtle: speed by caching it instead of using curl everytime.

A simple shell script (bash) to check weekly most popular anime sorted by views.

> Python version for the script is now available.

The script scrape from [hi10anime](https://hi10anime.com/)

## Dependencies (Bash)
- [awk](https://www.gnu.org/software/gawk/manual/gawk.html)
- [pup](https://github.com/ericchiang/pup)
- [sed](https://www.gnu.org/software/sed/manual/sed.html)
- [curl](https://curl.se/docs/)

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

## Dependencies (Python)
- [re](https://docs.python.org/3/library/re.html?highlight=re#module-re)
- [requests](https://requests.readthedocs.io/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [tabulate](https://pypi.org/project/tabulate/)

## Screenshot
![ani-list-demo](https://raw.githubusercontent.com/luqmannn/ani-list/main/screenshot.png)