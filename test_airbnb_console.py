#¡/usr/bin/env bash
# This script executes test cases for console application

file_path="console.py"
output_file="/tmp/ls_output.txt"
json_file="file.json"
get_db=$(cat "$json_file" | grep -o '{.*}')
uuid=$(cat "$json_file" | grep -oE '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}' | head -1)


#test do all without model name
echo "test do all without model name ..."
length=$(echo "all" | ./console.py | wc -c)
if [ "$length" -gt 0 ] 
then
    echo "pass"
else
    echo "fail"
fi

#test do update without model name
echo ""
echo "test do update without model name ..."
length=$(echo "update" | ./console.py | wc -c)
expected_length=$(echo "** class name missing **" | wc -c)

if [ "$length" -eq "$expected_length" ] 
then
    echo "pass"
else
    echo "fail"
fi

#test do update with unknown model name
echo ""
echo "test do update without model name ..."
expected_length=$(echo "** class doesn't exist **" | wc -c)
got_length=$(echo "update MyModel" | ./console.py | wc -c)

if [ "$expected_length" -eq "$got_length" ] 
then
    echo "pass"
else
    echo "fail"
fi

#test do update with model name but no id
echo ""
echo "test do update without model name ..."
expected_length=$(echo "** instance id missing **" | wc -c)
got_length=$(echo "update BaseModel" | ./console.py | wc -c)

if [ "$expected_length" -eq "$got_length" ] 
then
    echo "pass"
else
    echo "fail"
fi

#test do update with model name but non existing id
echo ""
echo "test do update with model name and non existing id..."
expected_length=$(echo "** no instance found **" | wc -c)
got_length=$(echo "update BaseModel 121212" | ./console.py | wc -c)

if [ "$expected_length" -eq "$got_length" ] 
then
    echo "pass"
else
    echo "fail"
fi

#test do update with model name and id but no attribute name
echo ""
echo "with model name and $uuid but no attribute name"
expected_length=$(echo "** attribute name missing **" | wc -c)
got_length=$(echo "update BaseModel $uuid" | ./console.py | wc -c)

if [ "$expected_length" -eq "$got_length" ] 
then
    echo "pass"
else
    echo "fail"
fi

#test do update with model name, id, attribute name but no attr value
echo ""
echo "test do update with model name, id, attribute name but no attr value"
expected_length=$(echo "** value missing **" | wc -c)
got_length=$(echo "update BaseModel $uuid first_name" | ./console.py | wc -c)

if [ "$expected_length" -eq "$got_length" ] 
then
    echo "pass"
else
    echo "fail"
fi

