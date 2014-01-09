# Program to calculate estimated dates from Spiceworks Tickets
import os # For filepaths
import pandas
import numpy # Needed for pandas
import time # Needed for date calculations
import datetime # Needed for date calculations
from pandas.tseries.offsets import * # For Bday (Business Days) utility
from openpyxl import workbook # For Excel writing



#Specify directories
originaldirectory = str('C:\Users\wliu\Desktop\Spiceworks\Original')
os.chdir(originaldirectory) #Change Local directory (where files go to)

"""
cleandirectory = str('C:\Users\wliu\Desktop\Spiceworks\Modified') # Not needed unless you need to clean unknown characters out
def write_files(myfilename):
    ### This function is not needed/used unless data is corrupt with unknown inputs, then call this to replace unknown characters###
    myinputfilelocation = os.path.join(originaldirectory, myfilename) #print myinputfilelocation #C:\Users\wliu\Desktop\Spiceworks\Original\Export2013-11-18.csv
    myoutputfilelocation = os.path.join(cleandirectory, myfilename)  #print myinputfilelocation #C:\Users\wliu\Desktop\Spiceworks\Modified\Export2013-11-18.csv
    myinputfile = open(myinputfilelocation, 'rb')
    myoutputfile = open(myoutputfilelocation, 'wb')

    # Take inputfile, read through all, clean out quotes (since some of the raw data has quotes inside), then write to output file
    for line in myinputfile:
        try:
            newline = unicode(line, errors='replace')
        except UnicodeDecodeError:
            print("Decode Error")
        newline = newline.encode('latin-1', errors='replace')
        myoutputfile.write(newline)
    myinputfile.close()
    myoutputfile.close()
"""

def modify_files(mydataframe):
    # Exclude specific columns
    mydataframe = mydataframe[mydataframe['Status']=='open']
    mydataframe = mydataframe[mydataframe['Category']!='Facilities']
    mydataframe = mydataframe[mydataframe['Division']!='Help Desk']
    mydataframe.fillna(0, inplace=True) # Fill NaN's with 0's
    mydataframe = mydataframe.sort(columns='IT Ranking', ascending=False) # Sort Desc
    #print mydataframe.values # print actual values instead of summary
    return mydataframe

def estimate_today():
    # <Take next highest ranked item and add 'Hours Remaining' to a new column 'Estimated Date'>
    #today = (time.strftime("%m/%d/%Y"))
    now = datetime.datetime.now()
    return now

def write_dataframe_to_csv(mydataframe, name):
    newname = name + '.csv' # Modify name to new csv name
    mydataframe.to_csv(newname) # Write dataframe to csv

def calc_hours(mydataframe):
    # Takes 'Hours Remaining' column, then creates an aggregate of hours into a new column

    #myhoursremaining = mydataframe['Hours Remaining'].sum() # Get total hours remaining
    #myitem = mydataframe.ix[[1563],'Hours Remaining'] # Prints Index (1563) and Hours Remaining (4)
    #mylist.append(myitem) # Take 'Hours Remaining' and add to list
    #print mylist #

    # Create two lists to hold current 'Hours Remaining' and Sum of 'Hours Remaining' (as it goes along column)
    mycurrenthours=[]
    myagghours=[]
    mytotalhours = 0

    for a in mydataframe['Hours Remaining']:     # Go through all 'Hours Remaining' list one at a time
        mycurrenthours.append(a) # mycurrenthours gets the current 'Hours Remaining' (e.g. 4, 2, 28, 2, 8, etc.)
        mytotalhours = sum(mycurrenthours) # add the current hours to an temporary total hours (i.e. doing a rolling sum)
        myagghours.append(mytotalhours) # add the rolling sum to a new list
    return myagghours

def estimate_days_projects(mylist, workinghours):
    
    mylist = map(int, mylist) # Convert all list items into int (from a numpy float)
    myprojecteddates = [] # Will hold all projected dates
    workinghoursperday = workinghours # Number of hours per working day

    now = datetime.datetime.now() # Get today's datetime
    #print now

    for a in mylist:
        #print a # this holds the aggregate hours remaining (e.g. 4, 6, 36, etc.)
        #print (a/workinghoursperday) # this holds the number of days remaining ()
        finishdate = (a/workinghoursperday) 
        finishdate = now + BDay(finishdate) # Returns the next business date that this item will be done
        finishdate = finishdate.strftime('%m/%d/%Y') # Format to mm/dd/yyyy
        myprojecteddates.append(finishdate) # Appends the next business date into list
    return myprojecteddates # returns a list of projected dates (e.g. '11/19/2013', '11/19/2013', '11/25/2013', '11/26/2013')

def concate_list(mydayslist, mydataframe):
    
    mydataframe['Projected Completion Date'] = mydayslist #Add mydayslist to a new column called 'Projected Date'
    return mydataframe

def create_projected_dates(mydataframe, workinghours):
    # Put in dataframe and number of available working hours per business day
    myhourslist = calc_hours(mydataframe) # Returns a list of aggregate hours sorted by IT Ranking (e.g. 4, 6, 34, 44, 46, 51, 76, 146)
    mydayslist = estimate_days_projects(myhourslist, workinghours) # Returns a list of projected dates per project (e.g. '11/19'2013', '11/25/2013')
    mydataframe = concate_list(mydayslist, mydataframe) # Returns dataframe with new column 'Projected Date' concatenated
    return mydataframe

def format_columns(mydataframe):
    
    #mycols = mydataframe.columns.tolist()
    #print mycols
    cols = [u'Ticket #', u'Create Date', u'Hours Remaining', u'IT Ranking', u'Executive Summary', u'Due At', 'Projected Completion Date', u'Created by', u'Assigned to', u'Category', u'Program', u'Status', u'Program Ranking', u'Division', u'Summary', u'Priority', u' Urgent', u'Time Spent in Minutes', u'Close Date']
    mydataframe = mydataframe.ix[:,cols]
    mydataframe = mydataframe.drop('Ticket #',1)
    return mydataframe


if __name__ == "__main__":

    # Specify file locations
    filename= 'Export2013-11-19.csv'

    mynewoutputfile = os.path.join(originaldirectory, filename)
    dataframe = pandas.io.parsers.read_table(mynewoutputfile, sep=',', quotechar='"', header=0, index_col=0, error_bad_lines=True, warn_bad_lines=True, encoding='latin-1')
    #print mydataframe
    
    cleandataframe = modify_files(dataframe) # Clean file (e.g. No HelpDesk tickets, No Facilities tickets, Open Tickets Only)

    # Slice up data by 'Division'
    programdf = cleandataframe[cleandataframe['Division']=='Web Development/Programming']
    reportdf = cleandataframe[cleandataframe['Division']=='Reporting/Routing']
    sysadmindf = cleandataframe[cleandataframe['Division']=='System Admin']

    hoursprojectsep = 10 # hours for project separation from 'Small Project' and Big Project' 
    # Slice up by 'Small Project' and 'Large Project'
    programdfs = programdf[programdf['Hours Remaining']<hoursprojectsep]
    programdfb = programdf[programdf['Hours Remaining']>=hoursprojectsep]
    reportdfs = reportdf[reportdf['Hours Remaining']<hoursprojectsep]
    reportdfb = reportdf[reportdf['Hours Remaining']>=hoursprojectsep]
    sysadmindfs = sysadmindf[sysadmindf['Hours Remaining']<hoursprojectsep]
    sysadmindfb = sysadmindf[sysadmindf['Hours Remaining']>=hoursprojectsep]

    # Run a few functions to create projected dates
    programdfs = create_projected_dates(programdfs, 2)
    programdfb = create_projected_dates(programdfb, 2)
    reportdfs = create_projected_dates(reportdfs, 2)
    reportdfb = create_projected_dates(reportdfb, 2)
    sysadmindfs = create_projected_dates(sysadmindfs, 2)
    sysadmindfb = create_projected_dates(sysadmindfb, 2)

    programdfs = format_columns(programdfs)
    programdfb = format_columns(programdfb)
    reportdfs = format_columns(reportdfs)
    reportdfb = format_columns(reportdfb)
    sysadmindfs = format_columns(sysadmindfs)
    sysadmindfb = format_columns(sysadmindfb)

    # Write dataframes to csv files
    #write_dataframe_to_csv(programdfs, 'Programming_Small')
    #write_dataframe_to_csv(programdfb, 'Programming_Big')
    #write_dataframe_to_csv(reportdfs, 'Reporting_Small')
    #write_dataframe_to_csv(reportdfb, 'Reporting_Big')
    #write_dataframe_to_csv(sysadmindfs, 'SystemAdmin_Small')
    #write_dataframe_to_csv(sysadmindfb, 'SystemAdmin_Big')

    # Write dataframes to xls files
    mywriter = pandas.ExcelWriter('projectoutput.xlsx')
    programdfs.to_excel(mywriter, sheet_name='programdfs') # Write dataframe to excel sheet_name
    programdfb.to_excel(mywriter, sheet_name='programdfb') # Write dataframe to excel sheet_name
    reportdfs.to_excel(mywriter, sheet_name='reportdfs') # Write dataframe to excel sheet_name
    reportdfb.to_excel(mywriter, sheet_name='reportdfb') # Write dataframe to excel sheet_name
    sysadmindfs.to_excel(mywriter, sheet_name='sysadmindfs') # Write dataframe to excel sheet_name
    sysadmindfb.to_excel(mywriter, sheet_name='sysadmindfb') # Write dataframe to excel sheet_name
    