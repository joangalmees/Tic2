#!/bin/bash
echo "Dim les paraules escites en el bucle"
Paraules=( Hola hem diven Joan )
for var in ${Paraules[@]}; do
printf $var 
done

