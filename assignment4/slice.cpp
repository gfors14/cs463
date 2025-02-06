#include <iostream>
#include <fstream>
#include <string>

using namespace std; //you got a problem????? Anyone got a problem with this???????? 


int main()
{
	string temp;
	string variable;
	int end_point;
	int line_number = 0;
	
	cout << "Please enter the name of the file you wish to slice: " << endl;
	cin >> temp;
	
	ifstream input(temp);
	
	cout << "Please enter the variable you want to perform the slice on: " << endl;
	cin >> variable;
	
	cout << "Please enter the endpoint of the slice: " << endl;
	cin >> end_point;
	
	cout << "Please enter the name of the output file: " << endl;
	cin >> temp;
	
	ofstream output(temp);
	output << "S(" << variable << ", " << end_point << ")\n\n"; //writes to file
	
	if(input.is_open())
	{
		while(!input.eof())
		{
			line_number++;
			getline(input, temp);
				
			if(temp.find(variable) != string::npos && line_number >= end_point) //checks if the variable is present, and if it is at or after the endpoint (startpoint in this case)
				output << line_number << " " << temp << "\n"; //writes to file
			else {}
			
			
		}
		input.close();
		output.close();
		
		
		
	}
	else
		cout << "Unable to open file! " << endl;
	
	
	
	
}
