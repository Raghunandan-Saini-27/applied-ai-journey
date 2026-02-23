#include <iostream>
#include <chrono>
#include <ctime>

using namespace std;

int main()
{
	int value;
	cout<<"Enter a number : ";
	cin>>value;

	string name;
	cout<<"Enter the username : ";
	cin>>name;
	//get current time

	auto now= chrono::system_clock::now();
	time_t current_time= chrono::system_clock::to_time_t(now);

	//processing
	int result=value*2;

	//output
	cout<<"Username :"<<name<<endl;
	cout<<"Result: "<<result<<endl;
	cout<<"Timestamp :"<<ctime(&current_time);
	return 0;
}