#!/usr/bin/env python
from csv import reader
import sys

for parts in reader(sys.stdin):
    try:
        vendor_name = parts[3].strip()
        transaction_amount = parts[2].strip()

        if not(vendor_name and transaction_amount):
            raise StandardError
        print ('%s\t%s') % (vendor_name, transaction_amount)
    except Exception as e:
        pass
