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
