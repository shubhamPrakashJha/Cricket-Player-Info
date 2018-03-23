#!/usr/bin/env python2.7

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Team, Player, User

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
engine = create_engine('sqlite:///teamplayerwithuser.db')
Base.metadata.bind = engine

# create staging zone for objects  loaded into the database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Shubham Prakash Jha", email="prakash.shubhamjha@gmail.com",
             picture='https://lh3.googleusercontent.com/-sUFh0NulfGk/'
                     'AAAAAAAAAAI/AAAAAAAAABw/vot7H1BUFeE/s120-p-rw-no/'
                     'photo.jpg')
session.add(User1)
session.commit()

# Players for Team India
team1 = Team(user_id=1,
             name="India",
             image_url="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC"
                       "3CAMAAAAGjUrGAAAApVBMVEX7dwATiAj///8AhQD7egAAAIAAAH0A"
                       "AHYAAG8AAHoAAHEAAHTq6vMAAHje3uzi4u4AAGmxsdDV1ebIyN/m5"
                       "u9dXaGYmMGvr8/Bwdnz8/hRUZulpcj5+f1YWJ9ZWaDU1OUsLIu6ut"
                       "ZBQZU1NZAzM5GKirokJIlLS5ljY6KdnceEhLa4uNRzc6wPD4Rubqx"
                       "jY6Q7O5IjI5AbG4x7e7GIiLm2ttu8vN85DFg5AAAGIklEQVR4nO2b"
                       "C3OiSBRGs71Lg9iCiLxBg0aNgcljnOT//7S9jUkmm2t2Zqu2ulPxO"
                       "1UyiGTqeur27Yf0xQUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                       "AAAAAAAAAAAAAAAADAf+Qv8J4LAd4DJ5zP4CRs07vV/fp+dZe2oe1"
                       "gxCdwEveOOxnJI6OJ6/Sx7ZDsOlEHOZHOwGg0Op7QlYOyGpVNJ+ra"
                       "JQ+UHBPHuUzT9NJxJpQy5Me9s2nFopPU1Ski1/tlLf1KhKLyZb3cr"
                       "4erbmovMGtO5lvKkdFEuq0IRE2ltaViW9N568qJ/mg7txWaLScd1R"
                       "FKhmC7q7UNohqOrahX20CnkJx0lmKz5GQzpvZRFseqERX6ODSWIhq"
                       "uqKKkFjTe2AnOjpPe1TXjWgSDlHBIkYU+VMP4ZB6Ia11V3IOV6Kw4"
                       "2VBH42w9UnHMhJ0+PLye6auVt9VSrGSKDSfV2JEyFDpHZkOK7HTjk"
                       "fQqBifVjA5KhFI648pCfBacBLrhhLPjm0br2GR0GNMr03lRLI4fzU"
                       "KdKYH5AC04+UZ9ylqI/fAmWNEhp/QofLKzy+nd6qiBPqehivxmPkD"
                       "zTm5G1HK0gNvhbUk9jZoWQnlKFFNqT1GpL9e3WhO1ntGN8QiNOwmp"
                       "mOwaXSbqK91uAo+OMhJzby4yqimFp9OkuKrpWDU7KinGp8rGnTTSm"
                       "RTHUyX1120oLxY7MfNmYkeVpNTVJJTP851i4sjGdIimnVCBHaXquX"
                       "AG/pIO006kXh17ce2lopvSZ0v/5QaVjsyXWdNObilN5mK+OX7PmHy"
                       "IxBWxH+V+HvmxcBOqKNPjEkqwoTspUW4Nx2jYSU2jNbmik/1is"
                       "JJNU8qWu9rvl96y9+uEMiSd6q5ZBAvdM61oPDupzQZp2ElEnY47F"
                       "Ah1X2orqdeLhaf6svDqXa+8RPRTPfMJyvuhpJQ0GxxFZoM07KSUc"
                       "vXyDTOvISu9nwi5mTs0ZpNqI0Xi92Sk8bLnu6KVlKXZIA07oQr7c"
                       "7RelNMkEMk0Uq7Yiu/0clU2TUSQTMvi9a6KqqzZIM06WU6cyWzWt"
                       "S8ri53rN1RSVVZV4V1QVdl8GonGd19WTlTbBTP6m6XRKM06yUbOi"
                       "P5R+1WTxjoV6sSTKnREoqIqU0nthEp6ia6pRZw2q72WR3+T/ft/+"
                       "z9j1oke1x8nMKq6msrrakndspvVC5VlXZappq5c6oCX+2tnelUds"
                       "8kxPr4364QGsdJ7aTiqWnv++KDEPlFpm+dtnqqkEuow9r119XqXJ"
                       "00PZc06uZLO5dt2UFSHxFlnRdZ1j+1j19HZ2kkOVfHmnuxymEYbx"
                       "KyT7Ztup1DzWZwvqXaEXRu3j4+Pbdx1NAOql3k8m6tXL9TxbI1Gad"
                       "bJd3IStNVm8SCpgRB0GDuLfRfHT09PcRztG2c8XKXDWD4sNlUbkJP"
                       "vRqO0nSczypMg69rHp8enrI2y4FSeyK+cJ7ye9KW8oiqSdySlzens"
                       "Upb9WdWTxcl+p0rUhnqdNt/ofmfe834nMRql3fHJfinCGxqfNG/GJ"
                       "zfD+ES+jk++ffHxyalxrPOPcexcOWc2jj0538mG+U7wwXxn9tXnO6"
                       "fnxR3Nix+e58XR2c2LP1o/SeeOcPX6iXOG6ycfrbPdNsM621yvs3l"
                       "nts724XrsIT7b9djfWrfvzmvdHr/vnKKUjvv7vwMq1zFdYT/Z78XR"
                       "+9+Lk/P4vRjPFZwCz59w8JzSCfA82wl+6JHbL5971KO1HzbCw/OxH"
                       "DxHzbH1vH3mDs/bh9vVieftw+F5e9fsStJPrO3LCH+5L8PaNjj7+3"
                       "fuq1ktvWH/jifrWXV/vvt3CHU7+Wif1+2Z7vMSej/g6MR+wNEZ7wc"
                       "cyO/e7Ru9y22HZN0JEeZp36zWq6ZPc+wv/pzACefiT/Ceiz/Ae+CE"
                       "AyccOOHACQdOOHDCgRMOnHDghAMnHDjhwAkHTjhwwoETDpxw4IQDJ"
                       "xw44cAJB044cMKBEw6ccOCEAyccOOHACQdOOHDCgRMOnHDghAMnHD"
                       "jhwAkHTjhwwoETDpxw4IQDJxw44cAJB044cMKBEw6ccOCEAyccOOH"
                       "ACQdOOHDCgRMOnHDghAMnHDjh/A2zGEMSVtPxGgAAAABJRU5ErkJg"
                       "gg==")
session.add(team1)
session.commit()

player1 = Player(user_id=1,
                 name="MS Dhoni",
                 role="Wicketkeeper batsman",
                 match="312",
                 runs="9898",
                 high_score="183*",
                 avg="51.55",
                 century="10",
                 fifty="67",
                 wickets="1",
                 bbm="1/14",
                 image_url="http://www.espncricinfo.com/inline/content/"
                           "image/1099927.html?alt=20",
                 team=team1)
session.add(player1)
session.commit()

player2 = Player(user_id=1,
                 name="Virat Kohli",
                 role="Top-order batsman",
                 match="202",
                 runs="9030",
                 high_score="183",
                 avg="55.74",
                 century="32",
                 fifty="45",
                 wickets="4",
                 bbm="1/15",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099912.html?alt=20",
                 team=team1)
session.add(player2)
session.commit()

player3 = Player(user_id=1,
                 name="Ravichandran Ashwin",
                 role="Bowling allrounder",
                 match="111",
                 runs="675",
                 high_score="65",
                 avg="16.07",
                 century="0",
                 fifty="1",
                 wickets="150",
                 bbm="4/25",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099922.html?alt=17",
                 team=team1)
session.add(player3)
session.commit()

player5 = Player(user_id=1,
                 name="Shikhar Dhawan",
                 role="Opening batsman",
                 match="96",
                 runs="4038",
                 high_score="137",
                 avg="44.86",
                 century="12",
                 fifty="23",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099915.html?alt=20",
                 team=team1)
session.add(player5)
session.commit()

player6 = Player(user_id=1,
                 name="Mohammed Shami Ahmed",
                 role="Bowler",
                 match="50",
                 runs="116",
                 high_score="25",
                 avg="10.54",
                 century="0",
                 fifty="0",
                 wickets="91",
                 bbm="4/35",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099933.html?alt=1",
                 team=team1)
session.add(player6)
session.commit()

# Players for Team Australia
team2 = Team(user_id=1,
             name="Australia",
             image_url="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/"
                       "2wCEAAkGBxITEhUQEhMWFhUWFRUXFhUXFxgWFRUXFxUXFxcXFhYY"
                       "HSggGBolGxUVITEiJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGxAQ"
                       "GC0fHiYtLS0tLS0tLS0rLS0tLS0tLS0uLS0tLS0tLS0tLS0tLS0t"
                       "LS0tLS0tLS0tLS0tLS0tLf/AABEIAL4BCgMBIgACEQEDEQH/xAAcA"
                       "AEAAgMBAQEAAAAAAAAAAAAABQYDBAcCAQj/xABJEAABAwIEAgYGBA"
                       "kLBQEAAAABAAIDBBEFEiExBlEHE0FhcYEUIjJSkaEjQnKxQ1NzgrL"
                       "B0eHwFTM1YmODkqLC0vEXJDQ2kxb/xAAZAQEAAwEBAAAAAAAAAAAA"
                       "AAAAAQMEAgX/xAAnEQACAwACAwAABgMBAAAAAAAAAQIDESExBBJBB"
                       "RMiMlGhQlJxFP/aAAwDAQACEQMRAD8A5oiIqzCEREAREQBERAEREJ"
                       "Pt0ug1NhvyG/wW8zCJrZnNEbfekIYPLNYoMNG6XU5RcPl+xkk/JMO"
                       "X/wCj7A+V1NU/CDu2ONn5R7pHebWgBVSuhHtjGUkX2Gq2Y6CZ20bv"
                       "MW+ZV9p8Aa3Qyu8I2tjb8Rc/NZ6nDKVgt1Yc7m8l5/zFUPzYLrk69"
                       "Dn7cNd9Z7G9xeCfg25WxHg5Oz3n7MTz8yAFdqdoyPexjQGAE2AFrm"
                       "3YsTq1S/Jf+pw2irs4ed7k577Mb+kVmHDh/FP85Yx9wKn31y1psQI"
                       "XK8ib6w4diRDuwa34H4z/ALGp/Jg/EA/35/2rJLiK8enlWqcyl+Vn"
                       "R4OHMG9O782cfrasLqODtjqW97Xxv+9ZH1pKwS1F91ZGT+nD8p/Ef"
                       "HUtIdOunZ9qG/6BWLGMObAWtEzZC5odlAc1zQdswOyxvlKl+kcg1s"
                       "budLF9xXZpqsc1yVtfF9XxSdhERAEREAREQBERAEREAREQBERASeF"
                       "YFNOx0zQ1kTPbmkcGRs8STcnwBUtQcPxGxY2WpPvD/t6f/G8Z3t72"
                       "heMR0wWJv4yq177bfBXKKoyxtbya0eQCz+RdKpfpLPVJaYsJ4bJ9q"
                       "RsLfcp2hp8HSvzOPlZbNRhdNA67IwXe++73nxc6/wAl7oaom608ak"
                       "O68ed9s7ccnhZ7JRNl2Id61qmuUfGVnhhzEJJKPLKlPTYpnG2crPg"
                       "T3yydW+mM0LjqbWLP6zX6BYMTkyMsNCoRlTM4hvWvsSB7ZAGvLbZX"
                       "+H6uTlJHFksOoTYFRw08jM5ayQtLiXB507G2VVxXDjHGDSUpLTe8z"
                       "yJZB+aD6vwXiv4iaZWRsZnhibl10zaDM4Dne6jq4/S5opHhhAIs4t"
                       "I7jbYr27J0enfJxOe/CLcw9u/bdRddN2Bb+J1Z1GYk8yblQxKw1Q3"
                       "kxXT5w+Er5dbFF1WcCbNkOhLCMze+x38F0Dh3o++nhqWTxzU4u64u"
                       "HHTQEbHVaYwOa6ZT6OakHZeXBXrG+DBHJJNPPHDG5xcG+3Jbt9UaD"
                       "zKptaY7nqg7J2F3tO7zZdODj2TKtweM0SNR4j71J8ePvWNHu08Q+R"
                       "UazV7Rzc0fNbXGDr10n9VrG/AIjX4/TIlERSXBERAEREAREQBERAE"
                       "REAREQBERAWbFv6JpO6pN/irXVMtbkQPuVPrH5sIZb8HU/fqr1KzP"
                       "FG4e40/5QsHmPmK/6WdrBhtM8tLw0lvMa28bbLJXYeXU8kx+o5rR5"
                       "rZ4fqI4D1jqgN5saC8nuPYrVjGLRhjWiHMXDOGkAae85q58bwPzJe"
                       "wk0ocnNqeke4Zg0lvvbN+J0UvQU4Dcx7VsVcsdQ5pfUkW/AlhbGPD"
                       "Lp8l7qZGhhykEDlssX4lU6pqCFSWais43Jd1lHxx3W1O0ucTzUhSY"
                       "dYXcu4yVcEihxcpM0qel8gsWIThosN1IV0oY2wVarJCSraY+70qtf"
                       "qjSnfcrGVlbCStmGhJW5tRRhxyYw2qbGcxgZI7+0Li0fmiwPnddDw"
                       "jit7KJ9RKWx3cWQxxtDW6al1gFQHsazc6rUrKxz8oJ0aLNHYPJW1X"
                       "NfC6FjrLtiuNuhhFRCWzMktm6wB1idw4HUKjYriLZTcQxxk79WXAH"
                       "xaTZYPSHAFoJyu3HYVpyOV9lrsfKHs5dm3gkeepibv64+RutfGps9"
                       "TO/nIR8NFI8JC0zpeyONzvlooFjr+t7xJ+JVZuqWI9IiIdBERAERE"
                       "AREQBERAEREAREQBERAT2HevQ1EXItePkFe+GH9ZSQk6+pl8xoqBw"
                       "tIOsfEdpGEee6ufR2+8ckJ3jfp4OuT9ywfiEdq1FlfLJujpMp1Gl7"
                       "25henGZ8pnJOY6NHYG8j3dysZoLxB1tVkwqg3c4eC8WPmW164Gv8h"
                       "N8kJR0VnOJbbNr4H9i08XjPsDt5K3+jX2Wq/DgHFx3WH/1WSn+bNH"
                       "boWeqKnR4SG+s4ar5WvDQrDVRcgoabDHvN3aBaa7lJ7JmedWLEVKt"
                       "JcVhpsKe82A8v+VaJaFjNbbKMrawN9kf87L06rtWRMM6knsjdpeDp"
                       "RG+QxuzNtkbb2iVXcaEsIs+Mx32zWB+AKlKrjR7GMhY0mNg9Yl5Dp"
                       "D26jZVHEZQ+Rz2lxBOmY3I7l6qpr9d0z2ygv2mCSW+5WFzll6glfH"
                       "Q23K6XHRmWGu5a8hWzI8Bakjr6DcrtF0ES1IeqoZ5dnSubG3w1uoV"
                       "gsLdwU1xL6jaekH1GdY/7TrbqHUm9LEgiIgCIiAIiIAiIgCIiAIiI"
                       "AiIgCIiAz0M2SRr+R/cr9wfUtixANd/N1ADTyu7Vpv8Aa+9c6VioZ"
                       "i+JrgfXiIse2wII+4fBV2QU1jJTxpn6LhpbNylZmU4AsFG8K4uKqm"
                       "jmv6xFnjk4aFTKrh4VUfhu92zAIABotc0l9Stx8gAuSABuToB5qJr"
                       "eIKZrSevjNuxr2uPwabqi/wAGmSXHKJVmfT7M0bAaKHxKS2jRfwWh"
                       "WcYU3vuHix4Hxso5/FUB9l4d+cAvEl+HSU9Z27oZ2a9fTSuvcEKGn"
                       "wtxUrUcQ8o7/nfuWjJxMR+C/wA37luqrcTDZGp9yIuXBrfUcfJakm"
                       "FTfVhPnb9ql38VAbxHyd+5eBxREd2PHwK2xlYlwjK6fFb5mQz8CqT"
                       "2ADvcFrSYDKN3N+N1ZP8A9BAR7Rae8WWvPVsds4HzXSnZ/Boh4njf"
                       "Jf2VmbB3Ddw+Cy4Jg465r3OuyO73aWFhey3Kp+6wYzUdTTdWNJJ9+"
                       "YZ4d60Vyk+yyVNcFwiCraszSyTH67jbuaDYfJYUAtpy0RXaUhERQQ"
                       "EREAREQBERAEREAREQBERAEREAW9g9V1cmvsu9V37VoogOr9H3EIp"
                       "pnQuP0b7eId9U2+AXVGVTnbCw+JX5ppKkkB41ezRzffZ+0LsvBXEz"
                       "ZogxzruaBY++3n4jYhZrXOPJopmumb+McIOlLnMrKhhdqWlwez/AR"
                       "aypeK8LVsVyYaarYOTBHLbuy21XS3Vo5qNq8QHYVnl5TwsnTBnJxL"
                       "TZsp6+jk5Zi6P4HVeaqkmAzFsVSz3gAHEeI7Vc8ahimGWRjXcrjUe"
                       "BVKq8OkgJfTudl7WE/wAXUxuU+Pphtrce/wCjQD4r2a6SJ3ukkj5p"
                       "JNM3ezxzCyvrY5tJGgO8LWWk/NGdDcK5L+TNOWH19Xfu7liLikjw7"
                       "W1ivBKsisMsuWHOWCV69yOXikpnSvEbBcn5DmV2juuLbN3A4i5xe9"
                       "1oo9XE7eCjcQrTPK6Y6X0YOTBt/HepHiCqa1oooT6rNZXD67uweSh"
                       "l1h6SWR5CIikkIiIQEREAREQBERAEREAREQBERAEREAREQHuGUtIc"
                       "Oz59yt/DdQ0gdUcjgcwt2O7fiqas9HVOjdnabeC5ktWA7BT42XDK7"
                       "Rw3HPvHcsVTXd6q1DirJmi5sR2jcH9YXysqJIz62oOzhsf3rz7PGx"
                       "6ix28ErV1/emF0vpV2RytbL2RyaB/2XDt8VXJqsHVb+E47TwuaW0v"
                       "WPDhZ8khJDthZosFZTQm+Sl2pvksjuBpvRJ88Y6+RzWsym+gF737L"
                       "qqYjgDqZl6qVjXdkLD1kh8beqB4ldLxniE5o6Tr2skc3M61hqRcMB"
                       "52KoXEeMQZzBPRtc5mnWNcY32531v5hep+RGMN0pu9P8SolYnvXuo"
                       "mZc5A4N7A4gn4heKOkkneI4mkn5DvJ7FnRnjBtmOJrpHBjBdx2AU1"
                       "XTiijMEZvUyD13D8G3l4rNVVUVA3qYbSVTh6z9xH581VdSS4m7ibu"
                       "J3JXWG6FXqGtt957yV9REO2EREICIiAIiIAiIgCIiAIiIAiIgCIiA"
                       "IiIAiIgCIiAyQTlpuCrFhuOgjJIAWncHby5FVlAoaIa0t1Xg+cGSm"
                       "OYdrD7TVCxTOjeHWs5pBAPMbLBQ4nJE4OY4i38fwFZKXF6SqsyqHV"
                       "v/GDQXPPkoUSmVXsV+oqXPcZHuLnE3c4/xovFfiL5CHSG7gLX7SBz"
                       "5q2SdH0j3/QTxyR7l9/ZHlusVW/DsONr+lVA7BYgHlYaBdciPjyb5"
                       "IfC+HZZR1kn0cW5c7S45NWSv4gZEw09ALDZ83afC+/iozGMbqKo/S"
                       "nKzcRNOn53NaDR5Iki+MYwAb23JJ1JO5PevqIhIREQgIiISEREICI"
                       "iAIiIAiIgCIiAIiIAiIgCIVauHej+tq2iVrRHEdpJDYEcw3cjvQlL"
                       "Sqouh/8AS65ytxCmL/d7fD2lUeIcCko5/R5HMc7TVjrjX3vdPcpxk"
                       "uLRFIuiM6JKksbIaiBocARmzDcXAuV5f0SVdiY54JDyDiPnqmMn0Z"
                       "z1Fv4zg89LIYaiMsfuOThzDtiFM8HcEzYg2R0UjGZCAc4Ot+VlByo"
                       "tvCroVs4pRmGaSBxBMby0kbG3aFMcM8GVlb60Mdo/xrzlZ5Hd3kFI"
                       "9f4ICOWRrSxsr2Md7TWktzeNjYrxGxrfZFu/cnxK6Kei6xyOxCma/"
                       "wB02vf/ABKscV8LS0D2skfG/MLtLHXNu9vYpOskuyCsiucHR3O6iF"
                       "f1sYYY+sy2dmtyvsqdTxueQ1jS5ziAGjVxJ0AsowhrDyivFd0azwU"
                       "/pNRUQxNy3LXZiQfd03KheEeF5K+V8MT2sLW5rvBsRfuTB6vcIFF0"
                       "V/RJUA2NXTg8jcH4LUxHo0khifM+rp8rGlxAuSbdgTGS4NFFRW7hj"
                       "gGashE4miiaSQ0SE5jbtt2Kab0P1JFxUwEcxmI+KYwoNnN0XQz0Tz"
                       "gX9Lp7eJVBqYg17mBwdlcRmGgNja4uowhrDEiIhyEREAREQBERAER"
                       "EAREQFp6NsEbV18ccguxgMjh72XYfGyufTTjssRioYiWMLMz8ulxs"
                       "1umw3VT6KcVZT4gwyEBsjTHmOwJ1F/h81ZenLCpOsiq2tJjyZHEC+"
                       "Ug3F/FT8Lkv08HKWj+O/msgcS8OJJJc3Um59odqx3XuMesPtN/SCF"
                       "afJ3fpNppJMJY2JjnuvCcrASbW10C5xwNgWIiridGyaNrXtL3ODmM"
                       "y39YEHe4uupcdYxNSYbHPA7K8GEagEEEaghYOHuJf5WpXxxzOpqpj"
                       "fWyHUG2jm5t2E+fgpL3HWQPTvUw5IItDLnLu8Msd/FZegb+aqfts/"
                       "RK5dxJQVEFTJHVZjKDq9xJzg7OBO4K6h0C/zVT9tn6JRdnEeZlInw"
                       "r0rGX0x9l9Q7N9kan5BdE6WsWdRUkVLTfR9Zdt26FrGjUA9hOmqoM"
                       "WJtpscdO7RralwceQdoT81eemrC3z00NTEM7YiScuvqOA9YW3GnzQ"
                       "R/azil7m535nU+Z7V6e8nck+JJ05arxm7V9/j5KCpad9wxhdw+1rR"
                       "cmlIAG5JJ0UNwnw5BhFOcRr7Ga3qt3yX2Y0Hd55qXw//wBfadv+1P"
                       "lqVDdH3FUWIQHDa7K55aA0nTrWgc/fC6NGro57xhxZNXy9Y/SMH6O"
                       "O+jBzPNytHQX/AOZL+R/1Kv8AHXB8tBLsXQOP0cn+l3Iqw9Bf/mS/"
                       "kf8AUoK4778nrpE4Qr56+aaGB7o3ZMrgRY6a7lUjGeH6qly+kxOjD"
                       "r5bka89irj0lcU1sGISxQ1MjGAMs0GwGl+SpOKY7U1GUVEz5A3bMb"
                       "2vyUPsibW/TRzHmfiu7cBf0ET/AGc361wcrvPAX9Bf3c/60RNWnCA"
                       "88z8Svi+BfVBU+wiIgCIiAIiIAiIgCIiAIiIArzw/0nVMMYgnY2pj"
                       "AsBJ7QG1ibWcPEKjL6pTOlJo6CeOMMvnbg8ee97kstfwsqxxRxD6Z"
                       "M2XqY4stgBGNwDcZj2/BQiFTpLm2XjinpCNZSCj6jJYsOfPmvkHK3a"
                       "qtgWLS0s7KiJ1nNPk4fWa7uKv2EcMUQihop2D0yphfKx5OsRt9G23f"
                       "ZQHR/gsctZLT1MebJDIS09j235d6EvTNxlxxHiEYD6QMkb7MofqOYO"
                       "mxXjgTjk4c2Rgh6zrHNd7WW1tNrLR4Iw6KbEIoJWB0Ze4FpvsL2Gim"
                       "OFuHqSWrrI5A1xiLxT07n5GyEOcACT2aAboFvZTsXrevnknIy9Y8uy"
                       "k7X3F+1WbhfpEq6NvUutNENmP3A5NduPApxHSyxRubPhLICfYmjL7N"
                       "5C+ZzXedlJcDNo6pswkoILwQGQODpLvc0H2vWsL9yjAt3s9S8cYY45"
                       "34RGXnf2LE+FtVXuLuKRW5GtpooWx6NyD1rcr6C3dZb/Crqaur4IXU"
                       "cMUZz52sLznttmzO0spzD8Chnmmhnw0U0LOsy1TXSMy5b5Sc5Ide3Y"
                       "p5J7I2DpHLKAYf6Pe0Rjz5+wk65bd6olPI5ha9ri1zbEOGhBGoI71P"
                       "cJYI2qrBDe8LC90j+zq2Hfz0Upxlh1M+mixGhjyQlzopWXJyuafVJ8"
                       "Rb4qMZy9a0k5elHrqb0erpGzXbZzs2XN/WtbQ"
                       "qvcF8VDD55JmxF4e3KGl1rC9wSbXPJbM+Ew/yNHV5B1xqMpfrct"
                       "10Wt0c4bFUV0cMzM7CyQlp5hpIUk69LPP0pwSOL5MNhe47udlc4+Z"
                       "bdYZOkqmIIGFwA6gGzP9iquC4H6TX+itFm9a/N/Vja4317gFP8XYV"
                       "RyUprKCPI2GZ0MrQb3GmWTU9qEuUsKPNIXOLjuSTbsGt9ByV3wLpE"
                       "NPQ+g9Rm9V7c+e3t37LKiooOE8YREUHP0IiIAiIgCIiAIiIAiIgCI"
                       "iAIiIApHh4wCpjdUkiJrgX5RmJDTcCw5lRyISi74j0iTGqM8cUGVr"
                       "x1ZdC3rAxugGfcaXW47i2jjxP06NrjHNEWzNy2cx7hZzmg781z1fE"
                       "0692XjA6rDaOo9NbUyzFuZzIRCWG7tg55NtL9igaZ1LPLNLUTPgc"
                       "95czLH1jRmcXG9iDe57FC2SynSNL7TcTwUlJPTtqZa10zcrQ9jmRR"
                       "6bgSEuJUXwLjcVKKnriR1sDmMsL+sRpfkqtZE1jSd4FxWOmrYqiY2"
                       "Y3PewudeQ7VM0fFsUoqKSuc99PI97oZNTJC4k2sN8vcqSvqaxpcMB"
                       "4igoaWfqXCSpkdkBcz1BECdTfe/aFsYTxlHJT1FJWMjjjkZ6hghDM"
                       "sg2Ja3cnTVUdfE1j2ZdaPFKOTC2UE0zo3tmL8wiMgI15LDwtX0VDX"
                       "xzNnfLGGSZndUWEFzSAA25JHeqgvqax7Fy4e4kgpG1c7PWqZnFsQc"
                       "27WxlxJLidLnks/D/ABw0tmpqyOFkE0bgTDC1hDraOIb7WqoqJo9m"
                       "fXtAJANxc2PMX0PwXxEQj6ERFBz9CIiEhERAEREB/9k=")
session.add(team1)
session.commit()

player1 = Player(user_id=1,
                 name="MJ Clarke",
                 role="Middle-order batsman",
                 match="245",
                 runs="7981",
                 high_score="130",
                 avg="44.58",
                 century="8",
                 fifty="58",
                 wickets="57",
                 bbm="5/35",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/817097.html?alt=1",
                 team=team2)
session.add(player1)
session.commit()

player2 = Player(user_id=1,
                 name="GJ Bailey",
                 role="Top-order batsman",
                 match="90",
                 runs="3044",
                 high_score="156",
                 avg="40.58",
                 century="3",
                 fifty="22",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/817087.html?alt=1",
                 team=team2)
session.add(player2)
session.commit()

player3 = Player(user_id=1,
                 name="PJ Cummins",
                 role="Bowler",
                 match="39",
                 runs="144",
                 high_score="36",
                 avg="12.00",
                 century="0",
                 fifty="0",
                 wickets="64",
                 bbm="4/24",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099509.html?alt=1",
                 team=team2)
session.add(player3)
session.commit()

player4 = Player(user_id=1,
                 name="JP Faulkner",
                 role="Bowling allrounder",
                 match="69",
                 runs="1032",
                 high_score="116",
                 avg="34.40",
                 century="1",
                 fifty="4",
                 wickets="96",
                 bbm="4/32",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1030005.html",
                 team=team2)
session.add(player4)
session.commit()

player5 = Player(user_id=1,
                 name="AJ Finch",
                 role="Top-order batsman",
                 match="33",
                 runs="1132",
                 high_score="156",
                 avg="37.73",
                 century="1",
                 fifty="7",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1099503.html?alt=1",
                 team=team2)
session.add(player5)
session.commit()

# Players for Team England
team3 = Team(user_id=1,
             name="England",
             image_url="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASIAAA"
                       "CuCAMAAAClZfCTAAAAM1BMVEX////OESQAAADMAANQUFDtvb9ABQv"
                       "WEiXNABXuwcPTAAf2xMY/AABKOzxTU1PhjZEXFxea6ikiAAAB4ElE"
                       "QVR4nO3aSU4DQQAEQYM3PBv+/2tB4jKWLOLYRmS8oJTnOrwHDqMHv"
                       "L4SUYmoRPST6L6dBlmXCyzrqG3bfZdoO4wyT1eY5mHjtl2i07AV5+"
                       "MbHM/Dxp1KJCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCW"
                       "iElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRl"
                       "YhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJ6D"
                       "US3ZzoNmzcPtE6n8e4fX4o0cfnbdC4ed0lWqbjICz03WjUtmnZJb"
                       "pcvfT/uV5KBCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRC"
                       "WiElGJqERUIioRlYhKRCWiElGJqERUIioRPSTqgvXMwwWrI98zD0e"
                       "+7qBPvcZjtlMxlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioR"
                       "lYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJq"
                       "ERUIioRlYhKRCWiElGJqERUIioRlYhKRCWiElGJqERUIioRlYhKR"
                       "CWiP5NoG7Zinq4wzcPGbbtE9+00yLpcYFlHbdvuu0T5RYmoRFQiK"
                       "hF9ARc3gVnveUO7AAAAAElFTkSuQmCC")
session.add(team3)
session.commit()

player1 = Player(user_id=1,
                 name="MM Ali",
                 role="Batting allrounder",
                 match="68",
                 runs="1395",
                 high_score="128",
                 avg="28.46",
                 century="3",
                 fifty="5",
                 wickets="54",
                 bbm="3/32",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/751925.html?alt=1",
                 team=team3)
session.add(player1)
session.commit()

player2 = Player(user_id=1,
                 name="JM Anderson",
                 role="Bowler",
                 match="194",
                 runs="273",
                 high_score="28",
                 avg="7.58",
                 century="0",
                 fifty="0",
                 wickets="269",
                 bbm="5/23",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1015875.html",
                 team=team3)
session.add(player2)
session.commit()

player3 = Player(user_id=1,
                 name="JM Bairstow",
                 role="Middle-order batsman",
                 match="37",
                 runs="1149",
                 high_score="141*",
                 avg="45.96",
                 century="2",
                 fifty="6",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/1015877.html",
                 team=team3)
session.add(player3)
session.commit()

player4 = Player(user_id=1,
                 name="GS Ballance",
                 role="Middle-order batsman",
                 match="16",
                 runs="297",
                 high_score="79",
                 avg="21.21",
                 century="0",
                 fifty="2",
                 wickets="0",
                 bbm="0",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/818163.html?alt=1",
                 team=team3)
session.add(player4)
session.commit()

player5 = Player(user_id=1,
                 name="IR Bell",
                 role="Top-order batsman",
                 match="161",
                 runs="5416",
                 high_score="141",
                 avg="37.87",
                 century="4",
                 fifty="35",
                 wickets="6",
                 bbm="3/9",
                 image_url="http://www.espncricinfo.com/inline/"
                           "content/image/565721.html?alt=1",
                 team=team3)
session.add(player5)
session.commit()

# # Players for Team
# team4 = Team(user_id=1,
# name="")
# session.add(team4)
# session.commit()
#
# player1 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player1)
# session.commit()
#
# player2 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player2)
# session.commit()
#
# player3 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player3)
# session.commit()
#
# player4 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player4)
# session.commit()
#
# player5 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team4)
# session.add(player5)
# session.commit()
#
# # Players for Team
# team5 = Team(user_id=1,
# name="")
# session.add(team5)
# session.commit()
#
# player1 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player1)
# session.commit()
#
# player2 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player2)
# session.commit()
#
# player3 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player3)
# session.commit()
#
# player4 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player4)
# session.commit()
#
# player5 = Player(user_id=1,
# name="",
#                  role="",
#                  match="",
#                  runs="",
#                  high_score="",
#                  avg="",
#                  century="",
#                  fifty="",
#                  wickets="",
#                  bbm = "",
#                  team=team5)
# session.add(player5)
# session.commit()
