#cat input/purchase_card_transactions_csv.csv | ./mapper.py 3 2| sort | ./reducer.py

rm -rf ./output

export HADOOP_HOME=/usr/local/Cellar/hadoop/2.4.1/libexec/share/hadoop/tools/lib

hadoop jar $HADOOP_HOME/hadoop-streaming-2.4.1.jar \
-file ./mapper.py -mapper 'mapper.py 3 2' \
-file ./reducer.py -reducer reducer.py \
-input ./input/purchase_card_transactions_csv.csv \
-output ./output