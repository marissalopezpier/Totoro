#!/usr/bin/env python3
"""
usage ./mpg.py MILES GALLONS [DATE]
Author : Marissa pier
Date   : 4 22 2019
Purpose: Python for gas mileage

"""

import os
#import sys
import argparse
import datetime
import csv
import statistics


def main():
    args = get_args()
    miles = args.miles
    gallons = args.gallons
    date = args.date
    datafile = args.datafile
    
    if miles <=0 and gallons <=0 :
        print('Miles and gallons must be greater than zero')
        exit(1)
    elif miles <= 0:
        print('Miles must be greater than zero')
        exit(1)    
    elif gallons <= 0:
        print('Gallons must be greater than zero')
        exit(1)
  
    elif not date:
        print('Date must have month, day, and year specified ordered(yearmonthday): i.e. 190422')
        exit(1)
            
    mpg = calc_mpg( miles, gallons )
    
    old_dates = []
    old_mpgs = []
    if os.path.exists(datafile):
        with open(datafile,'r') as fi:
            for row in csv.reader( fi, delimiter=',' ):
                if row:
                    old_dates.append(row[0])
                    old_mpgs.append(float(row[1]))
    if old_mpgs:
        old_avg_mpg = statistics.mean(old_mpgs)
    else:
        old_avg_mpg = None
    
    new_avg_mpg = statistics.mean(old_mpgs+[mpg])
    
    print('Old Average MPG:',old_avg_mpg)
    print('New MPG added:',mpg)
    print('New Average MPG:', new_avg_mpg)
    
    with open(datafile,'a') as fo:
        csv.writer(fo).writerow([date,mpg])
    

def calc_mpg( miles, gallons ):
    return miles/gallons

def check_date( date ):
    if len(date)!=6:
        return False
    try:
        datetime.datetime.strptime(date,'%y%m%d')
#        print(datetime.datetime.strptime(date,'%y%m%d'))
        return True
    except:
        return False



def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(description='Mileage per Gallon',formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
          'miles',
          metavar='MILES',
          help='miles of trip',
          type = float,
          default = '',
          )
    parser.add_argument(
          'gallons',
          help='gallons per car tank',
          metavar='GALLONS',
          type = float,
          default='',
          )
    parser.add_argument(
          '-d',
          '--date',
          help='Record by Date ',
          metavar='DATE',
          default=datetime.datetime.now().strftime('%Y%m%d'),
          )
    parser.add_argument(
          '-f',
          '--datafile',
          help='Data file location',
          metavar='FILE',
          default='./mpg.csv',
          )
    return parser.parse_args()


if __name__ == '__main__':
  main()
