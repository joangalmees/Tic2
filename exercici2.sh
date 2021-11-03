#!/bin/bash
echo "Escriu un nombre"
read nombre1
echo "Escriu un altre nombre"
read nombre2
if [ $nombre1 -gt $nombre2 ]; then
echo "El primer es més gran que el segon"
fi
if [ $nombre2 -gt $nombre1 ]; then
echo "El segon és més gran que el primer"
fi
