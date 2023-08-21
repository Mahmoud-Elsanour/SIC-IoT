#!/bin/bash

# Read the numbers and the operator
read -p "Enter the first number: " N1
read -p "Enter the Operation: " O
read -p "Enter the second number: " N2

# Choose the operation
case $O in
	-)
		echo -e "The result is: $(($N1 - $N2))"
	;;

	+)
		echo "The result is: $(($N1 + $N2))"
	;;

	/)
		if [[ $N2 -eq 0 ]];
		then
			echo "Division on Zero is not allowed"
			exit 1
		fi
		echo "The result is: $(($N1 / $N2))"
	;;
		
	'*')
		echo "The result is: $(($N1 * $N2))"
	;;

	*)
		echo "Please Enter one of these operators: (+ - * /)"
	;;

esac

# Exit the program
exit 0
