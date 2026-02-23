# include <iostream>
# include <vector>

using namespace std ;

vector<int> clean_data(vector<int> data)
{
	vector<int> cleaned;
	for(int x:data)
	{
		if(x>=0)
		{
			cleaned.push_back(x);
		}
	}
	return cleaned;
}

vector<int> process_data(vector<int> data)
{
	vector<int> processed;
	for(int x:data)
	{
		processed.push_back(x*x);
	}
	return processed;
}

double analyze_data(vector<int> data)
{
	if(data.size()==0)
		return 0;
	
	int sum=0;
	for(int x:data)
		sum+=x;

	return (double)sum/data.size();
}

double pipeline(vector<int> raw)
{
	vector<int> step1 =clean_data(raw);
	vector<int> step2 =process_data(step1);
	double result =analyze_data(step2);
	return result;
}

int main()
{
	vector<int> raw={10,-5,3,-1,7,2};
	double output=pipeline(raw);

	cout<< "Final output :" << output <<endl;

	return 0;
}