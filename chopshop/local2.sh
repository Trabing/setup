#!/usr/bin/env bash

scp /home/kenso/.ssh/id_rsa.pub root@159.89.35.212:/etc/ssh/kensotrabing/authorized_keys

scp /home/kenso/Projects/setup/.credentials root@159.89.35.212:/home/kensotrabing/

ssh root@159.89.35.212