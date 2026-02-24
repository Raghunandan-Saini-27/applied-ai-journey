#include <iostream>

using namespace std;

int main()
{
	int age;
	cout<<"Enter the age :"<<endl;
	cin>>age;

	if(age<13)
	{
		cout<< "Child category"<<endl;
	}

	else if(age>=13 && age <=19)
	{
		cout<< "Teen category" <<endl;
	}

	else if(age>19 && age<=60)
	{
		cout<< "Adult category" <<endl;
	}

	else
	{
		cout<< "Senior Citizen category" <<endl;
	}
	return 0;
}