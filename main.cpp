#include<iostream>
#include<stdio.h>
#include<bitset>
#include<string>
#include<vector>
#include<stdlib.h>

using namespace std;

int oneCounter(int *binary, int number){
	int count=0;
	for(int i=0; i<number; ++i){
		if(binary[i] == 1){
			count++;
		}
	}
	return count;
}

int main(){
	int i;
	int number_of_var, number_of_minterms, no_of_dontCare;
	cout << "Enter number of variables" << endl;
	cin >> number_of_var;
	cout << "Enter the total number of minterms including don't care conditions" << endl;
	cin >> number_of_minterms;
	cout << "Enter the number of don't care" << endl;
	cin >> no_of_dontCare;

	int *minterms_decimal = (int *)malloc(number_of_minterms*(sizeof(int)));
	int *minterms_decimal_dontCare = (int *)malloc(no_of_dontCare*(sizeof(int)));

	/***Data Entering****/
 	cout << "Enter the minterms in ascending order"<< endl;
	for(int i=0; i<number_of_minterms; ++i)
		cin >> minterms_decimal[i];
	
	if(no_of_dontCare){
		cout << "Enter the don't care conditions in ascending order" << endl;
		for(int i=0; i<no_of_dontCare; ++i)
			cin >> minterms_decimal_dontCare[i];
	}
	/******/

	int **minterms_binary = (int **)malloc(number_of_minterms*(sizeof(int *)));
	for(i=0; i<number_of_minterms; ++i)
		minterms_binary[i] = (int *)malloc((number_of_var+4)*sizeof(int));

	//conversion of decimal to binary and stored in minterms_binary 2D array
	for(i=0; i<number_of_minterms; ++i){
		int d = minterms_decimal[i];
		for(int j=number_of_var-1; j>=0; --j){
			minterms_binary[i][j] = d%2;
			d = d/2;
		}	
	}
	
	for(i=0; i<number_of_minterms; ++i){
		minterms_binary[i][number_of_var] = oneCounter(minterms_binary[i], number_of_var);
		minterms_binary[i][number_of_var+1] = 0;
		minterms_binary[i][number_of_var+2] = minterms_decimal[i];
	}

	//to test the minterms_binary array
	for(i=0; i<number_of_minterms; ++i){
		for(int j=0; j<number_of_var+4; ++j){
			cout << minterms_binary[i][j];
		}
		cout << "  ";
	}
}