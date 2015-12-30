#!/usr/bin/python2.7
#
# Assignment2 Interface
#

import psycopg2
import os
import sys

# Donot close the connection inside this file i.e. do not perform openconnection.close()
def RangeQuery(ratingsTableName, ratingMinValue, ratingMaxValue, openconnection):
    if(ratingMinValue < 0.0):
        print "Please provide a rating value greater than or equal to 0. Exiting the program. Please try again."
        exit()
    if(ratingMaxValue > 5.0):
        print "Please provide a rating value less than or equal to 5.0. Exiting the program. Please try again."
        exit()
    cur = openconnection.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cur.fetchall()
    outputFile = 'RangeQueryOut.txt'
    file = open(outputFile, 'w')
    for each_table in tables:
        if not (each_table[0] == 'rangeratingsmetadata' or each_table[0] == 'roundrobinratingsmetadata'):
            cur.execute("SELECT * FROM %s WHERE Rating >= %f AND Rating <= %f" %(each_table[0] , ratingMinValue, ratingMaxValue))
            values = cur.fetchall()

            for each_value in values:
                file.write(str(each_table[0]) + ', ' + str(each_value[0]) + ', ' + str(each_value[1]) + ', ' + str(each_value[2]) +'\n')
    file.close()

def PointQuery(ratingsTableName, ratingValue, openconnection):
    if(ratingValue > 5.0 or ratingValue < 0.0):
        print "Please provide a rating value greater than or equal to 0.0 and less than or equal to 5.0. Exiting the program. Please try again."
        exit()
    cur = openconnection.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cur.fetchall()
    outputFile = 'PointQueryOut.txt'
    file = open(outputFile, 'w')
    for each_table in tables:
        if not (each_table[0] == 'rangeratingsmetadata' or each_table[0] == 'roundrobinratingsmetadata'):
            cur.execute("SELECT * FROM %s WHERE Rating = %f" %(each_table[0] , ratingValue))
            values = cur.fetchall()

            for each_value in values:
                file.write(str(each_table[0]) + ', ' + str(each_value[0]) + ', ' + str(each_value[1]) + ', ' + str(each_value[2]) +'\n')
    file.close()
