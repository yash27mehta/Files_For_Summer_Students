#!/bin/bash
#######################################################################################
# The purpose of this script is to submit several depdendent jobs. The job submission
# script will be the same; this just resubmits it several time for code restarting
# purposes.
#
#
#Authors: Christopher Neal and Yash Mehta
#
# Date: 02-11-2015
# Updated: 07-24-2019
# 
#######################################################################################

#This script should be executed in the directory that contains the job submission script.
# It takes 2 arguments:
# 1.)The name of the restart job submission script that you want to submit
# 2.)Number of times you want to submit the jobs 
#
# The code creates a file that contains all of the job IDs from the jobs that are submitted.
#
echo 'Running Dependent Job Submission Script'

echo "Submitting Job File: $1"

for (( i=1; i<=$2; i++))
do

  echo "Submitting Job: $i"

  if [ "$i" -eq "1" ]; then
    
    sbatch $1 | tee submission_temp.txt #Copy output from terminal into file(COPIES)
    one=$(tail submission_temp.txt | tr -dc '0-9') #Extract last numeric line of temp file
    #echo $one #For debugging
    
    echo $one > jobIDs.txt #Write job ID to file

  else
    
    sbatch -d afterany:$one $1 | tee submission_temp.txt
    two=$(tail submission_temp.txt | tr -dc '0-9')
    #echo $two #For debugging

    one=$two

    echo $one >> jobIDs.txt #Append job ID to file

  fi

done


#Clean up temporary files
rm -rf submission_temp.txt

echo 'Program Finished...Ending'
