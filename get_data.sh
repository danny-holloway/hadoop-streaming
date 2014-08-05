#!/bin/bash

curl -o purchase_card_transactions_csv.zip http://data.octo.dc.gov/feeds/purchase_card_transactions/purchase_card_transactions_csv.zip
unzip purchase_card_transactions_csv.zip -d ./input/
rm purchase_card_transactions_csv.zip
