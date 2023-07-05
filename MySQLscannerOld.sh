#!/bin/bash
#This script is designed to find hosts with MySQL installed

nmap -sT 192.168.1.159 -p 3306 > /dev/null -oG MySQLscan

cat MySQLscan | grep open > MySQLscan2

cat MySQLscan2