echo "Introdueix un nombre entre 0 i 9"
numero=("1","2","3","4","5","6","7","8","9")
echo "Digues un número"
read numero

for (( i=0; i<numero; i++ ))
do
printf $numero
echo $numero
done
