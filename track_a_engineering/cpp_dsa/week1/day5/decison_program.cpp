# include <iostream>
using namespace std;

string CheckEligibility(int age)
{
	if(age<0)
	{
		return "Invalid age.";
	}

	else if(age<18)
	{
		return "Not Eligible.";
	}

	else
	{
		return "Eligible";
	}

}



int main()
{
	int age;
	cout<<"Enter the age :"<<endl;
	cin>>age;

	string result=CheckEligibility(age);
	cout << "Result :"<<result<<endl;
	return 0;
}  