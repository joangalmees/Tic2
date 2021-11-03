echo "Escriu un nombre"
read nombre1
echo "Escriu un altre nombre"
read nombre2
if [ $nombre1 -gt $nombre2 ]; then
echo "El primer es més gran que el segon"
fi
if [ $nombre2 -gt $nombre1 ]; then
echo "El segon és més gran que el segon"
fi

echo "Escriu un nombre"
read nombre1
echo "Escriu un altre nombre"
read nombre2
if [ $nombre1 -gt $nombre2 ]; then
echo "El primer es més gran que el segon"
fi
if [ $nombre2 -gt $nombre1 ]; then
echo "El segon és més gran que el segon"
fi

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

nSecret1=$((RANDOM%21))
nSecret2=$((RANDOM%21))
echo "Digues el teu nom:"
read nom
echo "Els números secrets són $nSecret1 i $nSecret2"
if [ $nSecret1 -gt $nSecret2 ]; then
echo "$nSecret1 és major que $nSecret2"
fi
if [ $nSecret2 -gt $nSecret1 ]; then
echo "$nSecret1 és menor que $nSecret2"
fi 
if [ $nSecret1 = $nSecret2 ]; then
echo "Els dos nombres són iguals"
fi
