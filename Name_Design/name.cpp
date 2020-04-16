#include<iostream>
#include<fstream>
#include <thread>         // std::this_thread::sleep_for
#include <chrono>		  // std::chrono::seconds
using namespace std;

int main()
{
	char ch;
	fstream fin("name.txt", fstream::in);
	while (fin >> noskipws >> ch) 
	{
		cout << ch;
		std::this_thread::sleep_for (std::chrono::seconds(1));
	}

	return 0;
}