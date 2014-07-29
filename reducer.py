#!/usr/bin/env python
import sys

current_vendor = None
total_amount = 0.0

for l in sys.stdin:
    try:
        vendor_name, transaction_amount = l.strip().split('\t')
        transaction_amount = float(transaction_amount)

        if not current_vendor:
            current_vendor = vendor_name

        if vendor_name == current_vendor:
            total_amount += transaction_amount
        else:
            #print '%s\t%s' % (current_vendor, total_amount)
            total_amount = transaction_amount
            current_vendor = vendor_name
    except Exception as e:
        print e
        print l
        pass
print '%s\t%s' % (current_vendor, total_amount)