i=0
while read line
do
    array[ $i ]="$line"
    (( i++ ))
done < <(ls)

echo ${array[100]}
