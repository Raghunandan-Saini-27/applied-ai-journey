#include <iostream>
#include <string>
using namespace std;

//================ CONFIG LAYER =================//

const int MAX_LIMIT = 10000;
const int DAILY_LIMIT = 25000;

//================ DATA MODEL ===================//

struct User {
    string username;
    string pin;
    int balance;
    int daily_withdrawn;
};

//================ AUTH LAYER ===================//

bool authenticate(User &u) {
    string uname, pass;

    cout << "Enter username: ";
    cin >> uname;

    for(int i = 3; i > 0; i--) {
        cout << "Enter PIN: ";
        cin >> pass;

        if(uname == u.username && pass == u.pin) {
            cout << "\nAuthentication successful!\n";
            return true;
        } else {
            cout << "Wrong credentials. Attempts left: " << i-1 << "\n";
        }
    }
    return false;
}

//================ UI LAYER =====================//

void show_menu() {
    cout << "\n====== SYSTEM PANEL ======\n";
    cout << "1. Check Balance\n";
    cout << "2. Deposit\n";
    cout << "3. Withdraw\n";
    cout << "4. Exit\n";
}

//================ BUSINESS LOGIC ===============//

void check_balance(User &u) {
    cout << "Balance: " << u.balance << endl;
}

void deposit(User &u, int amount) {
    if(amount > 0) {
        u.balance += amount;
        cout << "Deposited: " << amount << endl;
    } else {
        cout << "Invalid amount\n";
    }
}

bool can_withdraw(User &u, int amount) {
    if(amount <= 0) return false;
    if(amount > u.balance) return false;
    if(amount > MAX_LIMIT) return false;
    if(u.daily_withdrawn + amount > DAILY_LIMIT) return false;
    return true;
}

void withdraw(User &u, int amount) {
    u.balance -= amount;
    u.daily_withdrawn += amount;
    cout << "Withdrawn: " << amount << endl;
}

//================ CONTROLLER ===================//

void controller(User &u) {
    bool system_on = true;

    while(system_on) {
        show_menu();
        int choice;
        cout << "Choose option: ";
        cin >> choice;

        if(choice == 1) {
            check_balance(u);
        }
        else if(choice == 2) {
            int amt;
            cout << "Enter deposit amount: ";
            cin >> amt;
            deposit(u, amt);
        }
        else if(choice == 3) {
            int amt;
            cout << "Enter withdraw amount: ";
            cin >> amt;

            if(can_withdraw(u, amt)) {
                withdraw(u, amt);
            } else {
                cout << "Withdrawal denied (rule violation)\n";
            }
        }
        else if(choice == 4) {
            cout << "System shutting down...\n";
            system_on = false;
        }
        else {
            cout << "Invalid option\n";
        }
    }
}

//================ MAIN (BOOT) ==================//

int main() {

    User user;
    user.username = "Raghu";
    user.pin = "sarghi919";
    user.balance = 10000;
    user.daily_withdrawn = 0;

    if(authenticate(user)) {
        controller(user);
    } else {
        cout << "System locked.\n";
    }

    return 0;
}