#!/bin/bash

# define process name
process_name=handle_signal.py

# get info containing process pid
process_pid_info=$(ps auxf |grep $process_name | grep python)

# get process pid
counter=0
process_pid=None

for temp_info in $process_pid_info
do
  echo $counter
  if [ $counter -eq "1" ];then
    process_pid=$temp_info
  fi
  counter=`expr $counter + 1`
done

echo $process_pid

# send signal 1
kill -SIGUSR1 $process_pid