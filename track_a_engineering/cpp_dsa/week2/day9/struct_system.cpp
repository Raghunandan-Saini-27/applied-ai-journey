#include <iostream>
#include <string>
using namespace std;

//----- Data Model -----//

const int max_limit=25000;
const int daily_limit=50000;
	
struct User
{
	string username;
	string pin;
	int balance;
	int daily_withdrawn;
};

//----- Functions -----//

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

void show_menu()
{
	cout<<"\n------ SYSTEM CONTROL PANEL -----\n";
	cout<<"1. Check Balance \n";
	cout<<"2. Deposit Amount \n";
	cout<<"3. Withdraw Amount \n";
	cout<<"4. Exit System \n";
}

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

int main()
{
	User user;
	user.balance=1000;
	user.daily_withdrawn=0;
	user.pin="sarghi919";
	bool system_on=false;

	system_on=authentication(user);

	while(system_on==true)
	{
		show_menu();

		int choice;
		cout<<"Enter the choice : \n";
		cin>>choice;
		switch (choice)
		{
		case 1:	
			check_balance(user);
			break;
			
		case 2:
			deposit_amount(user);
			break;

		case 3:
			withdraw_amount(user);
			break;

		case 4:
			cout<<"System shutting down...";
			system_on=false;
			break;

		default:
			cout<<"Invalid Option.";
			break;
		}
	}
}