#!/bin/bash

# Following is the example of the echo command
echo "This is an example of the echo command"
# echo "$COLUMNS x $LINES" $COLUMN => columns of the terminal
# echo "$COLUMNS x $LINES" $LINES => lines of the terminal
# Following explains the !! usage
#~/TRAINING/MYZEN/UDACITY/Courses/SHELLWORKSHOP shell_workshop* ❯ echo gaurav
# ~/TRAINING/MYZEN/UDACITY/Courses/SHELLWORKSHOP shell_workshop* ❯ echo !! --> echo the last command on the command prompt without executing
# ~/TRAINING/MYZEN/UDACITY/Courses/SHELLWORKSHOP shell_workshop* ❯ echo echo gaurav
#example of usage ;
current_list_of_dir_info="$(ls -d -- */)" #if no directory, throws: ls: */: No such file or directory
echo "Here is the list of the directories"
echo "$current_list_of_dir_info"
#current working directory
currentlyAt=$PWD #special env variable holding current directory value
echo "$currentlyAt"

# Following commands did not produce any output,on the other hand, if executed directly on the command, it produces valid output
# wasAt="$($OLDPWD)"
# echo "last working directory is given by :"
# echo "$wasAt"
