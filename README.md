# SC Beer Game Python
Python implementation for [MIT Beer Supply Chain game](https://mitsloan.mit.edu/teaching-resources-library/mit-sloan-beer-game-online). There are some changes compared to the original version.

Simplified version of this implementation: [MIM2022 Conference Paper](https://doi.org/10.1016/j.ifacol.2022.09.673) 

Author: Maxim Rozhkov [youtube channel](https://www.youtube.com/channel/UCxcUanIa5FKZf0FhUDAA5Dg), [HSE University profile](https://www.hse.ru/en/org/persons/25922950)

The supply chain game consists of administrator, who sets period and demand level and four players: Retailer, Distributor, Wholesaler and Plant

Running sequence (py or exe files): 
1. server: server3_stm
2. players & administrator: adm_remi_st, ret_remi_st, distr_remi_st, whole_remi_st, plant_remi_st

File structure (for administrator, same for other players): adm_remi_st.py (main logic), adm_remi_st_gui.py (GUI)

In case of executable file both logic and GUI are combined in adm_remi_st.exe

User interface (for Retailer):

<img src="https://user-images.githubusercontent.com/55400375/217362979-ea1a6c9e-51cb-4ed7-b373-be667b7370cd.png" width="622" height="499">

The GUI is made in Remi package [Remi](https://github.com/rawpython/remi)

Requirements:
```
remi==2022.7.27
xlwt==1.3.0
```
Passphrase for connection is set to "1". Default port for a server is "5555". Game statistics is written in Excel files

The game can be tested/run on localserver in browser. For in class playing I used VPS server in cheapest configuration: 1x2.2 GHz, 0.5Gb RAM, HDD, Debian 10 or Ubuntu 20.04 (any other linux server can be used too)

The code is based on Python Client-Server interaction tutorials by TechWithTim: [1](https://www.youtube.com/watch?v=-3B1v-K1oXE), [2](https://www.youtube.com/watch?v=3QiPPX-KeSc&t=2607s) 

To build exe files use pyinstaller package (example for Administrator player):
```
pyinstaller -F  adm_remi_st.py
```


