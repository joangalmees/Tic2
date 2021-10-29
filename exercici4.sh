#!/bin/bash
echo "Escriu un nombre de 0 a 100"
read nombre1
ncreat=$(($RANDOM%101))
echo "El nombre creat és $ncreat"
if [ $ncreat -gt $nombre1 ]; then
echo "El nombre creat és més gran que el teu"
fi
if [ $nombre1 -gt $ncreat ]; then
echo "El nombre teu és més gran que el nombre creat"
fi
