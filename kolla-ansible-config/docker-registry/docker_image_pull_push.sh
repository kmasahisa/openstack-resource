#!/bin/bash -ex


python3 image_check.py | tee a.txt

num=`wc -l a.txt | awk '{print $1}'`
cat a.txt | awk '{print $1}' > list.txt

cat list.txt | while read line
do
  docker pull linaro/$line:queens-20180131
  docker tag linaro/$line:queens-20180131 10.101.16.3:5000/linaro/$line:queens-20180131
  docker push 10.101.16.3:5000/linaro/$line:queens-20180131
done

rm -f a.txt
rm -f list.txt

