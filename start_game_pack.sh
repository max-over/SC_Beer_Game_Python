#!/bin/bash

# USAGE: ./start_game_pack.sh <unique_team_number>
# EXAMPLE: ./start_game_pack.sh 1

PACK_NUM=${1:-0}
SERVER_PORT=$((5555+PACK_NUM))
ADM_PORT=$((8084+PACK_NUM*10))
DISTR_PORT=$((8085+PACK_NUM*10))
WHOLE_PORT=$((8086+PACK_NUM*10))
PLANT_PORT=$((8087+PACK_NUM*10))
RET_PORT=$((8089+PACK_NUM*10))

echo "Starting game pack with ports $SERVER_PORT $ADM_PORT $DISTR_PORT $WHOLE_PORT $PLANT_PORT $RET_PORT"

nohup python3 server3_stm.py $SERVER_PORT &
nohup python3 adm_remi_st.py $ADM_PORT $SERVER_PORT &
nohup python3 distr_remi_st.py $DISTR_PORT $SERVER_PORT &
nohup python3 whole_remi_st.py $WHOLE_PORT $SERVER_PORT &
nohup python3 plant_remi_st.py $PLANT_PORT $SERVER_PORT &
nohup python3 ret_remi_st.py $RET_PORT $SERVER_PORT &

echo "Started game pack with ports $SERVER_PORT $ADM_PORT $DISTR_PORT $WHOLE_PORT $PLANT_PORT $RET_PORT"
