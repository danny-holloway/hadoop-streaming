#cat input/purchase_card_transactions_csv.csv | ./mapper.py | sort | ./reducer.py

rm -rf ./output

hadoop jar /usr/local/Cellar/hadoop//2.4.1/libexec/share/hadoop/tools/lib/hadoop-streaming-2.4.1.jar \
-file ./mapper.py -mapper mapper.py \
-file ./reducer.py -reducer reducer.py \
-input ./input/purchase_card_transactions_csv.csv \
-output ./output