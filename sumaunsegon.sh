#exercici condiconals, suma un segon

num1=1

echo "Digués un numero1 en hores"
read numero1
echo "Digues un numero2 en minuts"
read numero2
echo "Digues un numero3 en segons"
read numero3

echo $numero1:$numero2:$numero3
echo "Suma un segon"
let suma=$numero3+$num1
echo $numero1:$numero2:$suma 
