echo "escriu lletres separades que contenguin alguna h"
read paraules
conta=0
for var in ${paraules[@]}
do
if [ $var = h -o $var = H ]
then
let conta=$conta+1
fi
done
echo "Hi ha: $conta h(s)."
