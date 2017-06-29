to run my_file_cutter.py it needs a t1.txt file

generate t1.txt by the following command

awk 'BEGIN{for (i = 0; i < 10000000; i++) {print "123.123.123.123"} }' > t.txt

<br/>

cat t.txt | tr '[.]' '[\t]' > t1.txt
