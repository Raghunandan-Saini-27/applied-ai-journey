#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int MAX_LIMIT=10000;
const int DAILY_LIMIT=25000;

//======== DATA MODEL =======//

struct User
{
	string username;
	string pin;
	int balance;
	int daily_withdrawn;
};

//======== USER REGISTRY =======//

void seed_users(vector<User> &users)
{
	users.push_back({"Raghu","1111",10000,0});
	users.push_back({"Amit","2222",8000,0});
	users.push_back({"Neha","3333",15000,0});
}

User* find_user(vector<User> &users,string username)
{
	for(auto &u :users)
	{
		if(u.username==username)
		{
			return &u;		// return adress
		}
	}
}

//======== AUTH =======//

User* authentication(vector<User> &users)
{
	string uname,pass;
	
	cout<<"Enter username : ";
	cin>>uname;

	User* user=find_user(users,uname);
	if(user==nullptr)
	{
		cout<< "User not found. \n";
		return nullptr;
	}

	for(int i=3;i>0;i--)
	{
		cout<<"Enter PIN : ";
		cin>>pass;
	

		if(pass==user->pin)
		{
			cout<<"Authentication successful! \n";
			return user;
		}

		else
		{
			cout<<"Wrong PIN. Attempts left : "<<i-1<<endl;
		}
	}
	return nullptr;
}

//======== UI ========//

void show_menu()
{
	cout<<"\n======== SYSTEM PANEL =======\n";
	cout<<"1. Check Balance\n";
	cout<<"2. Deposit \n";
	cout<<"3. Withdraw \n";
	cout<<"4. Exit \n";
}

//======== LOGIC =======//

void check_balance(User &u)
{
	cout<<"Balance : "<<u.balance<<endl;
}

void deposit(User &u, int amount)
{
	if(amount>0)
	{
		u.balance+=amount;
		cout<<"Deposited : "<<amount<<endl;
	}
	else
	{
		cout<<"Invalid Amount\n";
	}
}

bool can_withdraw(User &u,int amount)
{
	if(amount<=0) return false;
	if(amount>u.balance) return false;
	if(amount>MAX_LIMIT) return false;
	if(u.daily_withdrawn+amount>DAILY_LIMIT) return true;
}

void withdraw(User &u,int amount)
{
	u.balance-=amount;
	u.daily_withdrawn+=amount;
	cout<<"Withdrawn : "<<amount<<endl;
}

void controller(User &u)
{
	bool running=true;

	while(running)
	{
		show_menu();
		int choice;
		cout<<"Choose option : ";
		cin>>choice;

		if(choice==1)
		{
			check_balance(u);
		}

		else if(choice==2)
		{
			int amt;
			cout<<"Enter deposit amount : ";
			deposit(u,amt);
		}

		else if(choice==3)
		{
			int amt;
			cout<<"Enter withdraw amount : ";
			cin>>amt;

			if(can_withdraw(u,amt))
			{
				withdraw(u,amt);
			}

			else
			{
				cout<<"Withdrawl denied.\n";
			}
		}

		else if(choice==4)
		{
			running=false;
			cout<<"Session ended.\n";
		}

		else
		{
			cout<<"Invalid option. \n";
		}
	}
}


//======= MAIN() =======//

int main()
{
	vector<User> users;
	seed_users(users);
	User* logged_in_user=authentication(users);
	if(logged_in_user!=nullptr)
	{
		controller(*logged_in_user);		//derefernced pointer
	}
	else
	{
		cout<<"Acess denied.\n";
	}
	return 0;
}