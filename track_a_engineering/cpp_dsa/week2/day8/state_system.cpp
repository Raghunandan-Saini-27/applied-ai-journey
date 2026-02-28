#include <iostream>

using namespace std;

bool verify_pin();

int main()
{
	//-----System State-----//
	int balance=1000;		//state variable
	bool system_on=false;	//control flag
	int daily_limit=25000;
	int daily_withdrawn=0;

	string name;
	cout<<"Enter the Username :\n";
	cin>>name;

	int i;
	for(i=3;i>=1;i--)
	{
	system_on=verify_pin();
	if(system_on==true)
	{
		break;
	}
	
	else
	{	
		cout<<i-1<<" Chances Remaining.\n";
	}
	}

	while(system_on==true)
	{
		cout<<"\n===== SYSTEM CONTROL PANEL =====\n";
		cout<<"\n===== USER : "<<name<<" =====\n";
		cout<<"1. Check Balance\n";
		cout<<"2. Add Money\n";
		cout<<"3. Withdraw Money\n";
		cout<<"4. Exit system\n";
		cout<<"Choose Option : \n";
	
		int choice;
		cin>>choice;
	
		switch(choice)
		{
			case 1:
			{
				cout<<"Current Balance : "<<balance<<endl;
				break; 
			}

			case 2:
			{
				int add;
				cout<<"Enter amount to enter : \n";
				cin>>add;
			
				if(add>0)
				{
					balance+=add;		//State Update
					cout<<"Money Added Sucessfully : "<<add<<"$"<<endl;
				}

				else
				{
					cout<<"Invalid Amount.\n";
				}
				break;
			}

			case 3:
			{
				int withdraw;
				int max_limit=10000;
				cout<<"Enter amount to withdraw : \n";
				cin>>withdraw;

				if(withdraw<=balance)
				{
					if(withdraw<=max_limit)
						if(daily_withdrawn+withdraw<=daily_limit)
						{
						balance-=withdraw;	//State Update
						daily_withdrawn+=withdraw;
						cout<<"Withdrawl Successful : "<<withdraw<<endl;
						}

						else
						{
							cout<<"Withdrawl Unsucessful(Reached Daily Limit.Try Again Tommorow!)";
						}

					else
					{
						cout<<"Withdrawl Unsuccessful(Exceeding Max Withdrawl Limit.)\n";
					}
				}

				else
				{
					cout<<"Invalid Withdrawl(Insuffecient Amount!)\n";
				}
				break;
			}
			
			case 4:
			{
				cout<<"System Shutting Down...\n";
				system_on=false;	//Control System Stop
				break;
			}

			default:
				cout<<"Invalid Option.\n";
		}	
	}
	return 0;
}

bool verify_pin()
{
	string pin;
	cout<<"Enter the PIN : \n";
	cin>>pin;

	if(pin=="knxq6y")
	{
		cout<<"Correct Pin(You may proceed further).\n";
		return true;
	}

	else 
	{
		cout<<"Wrong Pin(Try Again!).\n";
		return false;
	}
}