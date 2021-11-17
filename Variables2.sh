nSecret=$(($RANDOM%11));echo $nSecret
echo "Introdueix un nombre entre 0 i 10: ";read nomUsuari

while [ "$nomUsuari" != "$nSecret" ]; do
if [ "$nomUsuari" -gt "$nSecret" ]; then
echo "El nombre a endivinar és menor"
echo "Introdueix un nombre entre 0 i 10: "; read nomUsuari
else
echo "El nombre a adivinar és major"
echo "Introdueix un nombre entre 0 i 10: "; read nomUsuari
fi
done
echo "Has endivinat el nombre"
