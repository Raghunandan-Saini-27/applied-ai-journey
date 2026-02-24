#include <iostream>
using namespace std;

/* ----Validation Layer----*/

bool validate_inputs(int marks,int attendance,int discipline)
{
	if(marks<0 || marks>100)
	{
		return false;
	}

	if(attendance<0 || attendance>100)
	{
		return false;
	}

	if(discipline<0 || discipline>2)
	{
		return false;
	}

	return true;

}

/*-----Decision Engine----*/

string decision_engine(int marks,int attendance,int discipline)
{
	// Guard clauses
	if(!validate_inputs(marks,attendance,discipline))
	{
		return "Invalid Input Data.Try Again!";
	}

	if(discipline>1)
	{
		return "Rejected (Severe Disciplinary Record)";
	}

	if(attendance<60)
	{
		return "Fail (Low attendance)";
	}

	if(marks>=85 && attendance>=75)
	{
		return "Excellent";
	}

	if(marks>=70)
	{
		return "Good";
	}

	if(marks>=50)
	{
		return "Pass";
	}

	else
	{
		return "Fail";
	}
}

/*----Inference Layer----*/

int main()
{
	int marks,attendance,discipline;
	cout<<"Enter the Marks (0-100) : "<<endl;
	cin>>marks;

	cout<<"Enter the Attendance (0-100) : "<<endl;
	cin>>attendance;

	cout<<"Enter the Discipline (0=clean ,1=warning ,2=Severe) : "<<endl;
	cin>>discipline;

	string result=decision_engine(marks,attendance,discipline);
	cout<<"\nDecision Result : "<<result<<endl; ;
	return 0;
}