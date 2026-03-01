#include <iostream>
#include <string>
using namespace std;

//----- Config Layer -----//

const int max_limit=25000;
const int daily_limit=50000;
	
//----- Data Model -----//

struct User
{
	string username;
	string pin;
	int balance;
	int daily_withdrawn;
};

//----- Auth Layer -----//

bool authentication(User &u)
{
	string password;
	string username;
	cout<<"Enter the username : \n";
	cin>>username;

	for(int i=3;i>=1;i--)
	{
		cout<<"Enter the password : \n";
		cin>>password;

		if(password==u.pin)
		{
			cout<<"Correct Password.\n"<< username <<" Logged in!\n";
			return true;
		}

		else
		{
			cout<<"Wrong Password. Chances Remaining : "<<i-1<<endl;
		}
	}
	return false;
	
}

//------ UI Layer  -----//

void show_menu()
{
	cout<<"\n------ SYSTEM CONTROL PANEL -----\n";
	cout<<"1. Check Balance \n";
	cout<<"2. Deposit Amount \n";
	cout<<"3. Withdraw Amount \n";
	cout<<"4. Exit System \n";
}

//----- Business Logic-----//

void check_balance(User &u)
{
	cout<<"Balance : \n"<<u.balance<<endl;
}

void deposit_amount(User &u)
{
	int amount;
	cout<<"Enter the amount to be added : \n";
	cin>>amount;

	if(amount>0)
	{
		u.balance+=amount;
		cout<<"Deposited : \n"<<amount<<endl;
	}

	else
	{
		cout<<"Invalid Amount. \n";
	}
}

void withdraw_amount(User &u)
{
	int withdraw;
	cout<<"Enter the amount to be withdrawn : \n";
	cin>>withdraw;

	if(withdraw<=0)
	{
		cout<<"Invalid amount.\n";
	}
	
	else if(withdraw>u.balance)
	{
		cout<<"Insuffecient Balance.\n";
	}

	else if(withdraw>max_limit)
	{
		cout<<"Max Transaction Limit Exceeded.\n";
	}

	else if(u.daily_withdrawn+withdraw>daily_limit)
	{
		cout<<"Daily Limit Reached.Try again Tommorow!\n";
	}

	else
	{
		u.balance-=withdraw;
		u.daily_withdrawn+=withdraw;
		cout<<"Amount withdrawn sucessfully : \n"<<withdraw<<endl;
	}

}

//----- Controller -----//

void controller(User &u)
{
	bool system_on=true;

	while(system_on)
	{
		show_menu();

		int choice;
		cout<<"Enter the choice : \n";
		cin>>choice;
		switch (choice)
		{
		case 1:	
			check_balance(u);
			break;
			
		case 2:
			deposit_amount(u);
			break;

		case 3:
			withdraw_amount(u);
			break;

		case 4:
			cout<<"System shutting down...\n";
			system_on=false;
			break;

		default:
			cout<<"Invalid Option.\n";
		}
	}
}

//----- MAIN ------//

int main()
{
	User user;
	user.username="Raghu";
	user.balance=1000;
	user.daily_withdrawn=0;
	user.pin="sarghi919";

	if(authentication(user)==true)
	{
		controller(user);
	}

	else
	{
		cout<<"System Locked.\n";
	}
	return 0;
}