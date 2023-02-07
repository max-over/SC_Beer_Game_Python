# SC Beer Game Python
Python implementation for MIT Beer Supply Chain game. There are some changes compared to the original version.

Simplified version of this implementation: [MIM2022 Conference Paper](https://doi.org/10.1016/j.ifacol.2022.09.673) 

Author: Maxim Rozhkov [My youtube channel](https://www.youtube.com/channel/UCxcUanIa5FKZf0FhUDAA5Dg), [HSE University profile](https://www.hse.ru/en/org/persons/25922950)

The supply chain game consists of administrator, who sets the period and demand level and four players: Retailer, Distributor, Wholesaler and Plant

The GUI is made in Remi package [Remi](https://github.com/rawpython/remi)

Requirements:
```
remi==2022.7.27
xlwt==1.3.0
```
Passphrase for connection is set to "1". Default port for a server is "5555".

The game can be tested/run on localserver in browser. For in class playing I used VPS server in cheapest configuration: 1x2.2 GHz, 0.5Gb RAM, HDD, Debian 10 or Ubuntu 20.04 (any other linux server can be used too)

The code is based on Python Client-Server interaction tutorials by TechWithTim: [1](https://www.youtube.com/watch?v=-3B1v-K1oXE), [2](https://www.youtube.com/watch?v=3QiPPX-KeSc&t=2607s) 
