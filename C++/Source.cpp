#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#include <set>
#include <string>
#include <stdio.h>
#include <math.h>

using namespace std;

vector<char> OPERATION = { '!', '|', '-', '&', '(', ')' };

bool isDigit(string str) 
{
    try 
    {
        stoi(str);
        return true;
    }
    catch (exception e) 
    {
        return false;
    }
}

vector<int> negat(vector<int> A) 
{
    vector<int> result ;
    for (int integer : A) 
    {
        if (integer == 1) 
        {
            result.push_back(0);
        }
        else
        {
            result.push_back(1);
        }
    }
    return result;
}

int priority(string op) 
{
    if (op.compare("(") == 0) return 0;
    if (op.compare("-") == 0) return 1;
    if (op.compare("|") == 0) return 2;
    if (op.compare("&") == 0) return 3;
    if (op.compare("!") == 0) return 4;

}



vector<vector<int>> create_bin_table(int size)
{
    vector<vector<int>> arr;
    for (int i = 0; i < size; i++)
    {
        arr.push_back(vector<int>());
        for (int l = 0; l < pow(2, i); l++)
        {
            double flor = floor(pow(2, size) / (pow(2, i + 1)));
            for (int k = 0; k < flor; k++)
            {
                arr[i].push_back(0);
            }
            for (int k = 0; k < flor; k++)
            {
                arr[i].push_back(1);
            }
        }

    }

    return arr;
}

pair<vector<string>, vector<vector<int>>> parse_expression(vector<string> expression)
{
    vector<char> array;
    for (int i = 0; i < expression.size(); i++)
    {
        string a = expression[i];
        for (int j = 0; j < a.size(); j++)
        {
            array.push_back(a[j]);
        }
    }
    vector<string> pars_arr;
    string current_variable = "";
    vector<string> array_variable;
    for (int i = 0; i < array.size(); i++)
    {
        if (array[i] == '>')
        {
            current_variable = "";
        }
        else if (find(OPERATION.begin(), OPERATION.end(), array[i]) == OPERATION.end())
        {
            current_variable += array[i];
        }
        else
        {
            pars_arr.push_back(current_variable);
            array_variable.push_back(current_variable);
            current_variable = "";
        }
        if (find(OPERATION.begin(), OPERATION.end(), array[i]) != OPERATION.end())
        {
            string s;
            s = array[i];
            pars_arr.push_back(s);
        }
    }

    pars_arr.push_back(current_variable);
    array_variable.push_back(current_variable);
    
    pars_arr.erase(std::remove(pars_arr.begin(), pars_arr.end(), ""), pars_arr.end());
    array_variable.erase(std::remove(array_variable.begin(), array_variable.end(), ""), array_variable.end());

    set<string> set(array_variable.begin(), array_variable.end());
    array_variable.assign(set.begin(), set.end());
    sort(array_variable.begin(), array_variable.end());

    for (int i = 0; i < array_variable.size(); i++)
    {
        for (int j = 0; j < pars_arr.size(); j++)
        {
            if (array_variable[i] == pars_arr[j])
            {
                pars_arr[j] = std::to_string(i);
            }
        }
    }

    return make_pair(pars_arr, create_bin_table(array_variable.size()));
}

vector<string> rpn(vector<string> expression)
{
    vector<string> arr = parse_expression(expression).first;
    vector<string> operations;
    vector<string> result;

    for (int i = 0; i < arr.size(); i++)
    {
        if (arr[i].compare("(") == 0)
        {
            operations.push_back(arr[i]);
        }
        else if (find(OPERATION.begin(), OPERATION.end(), arr[i].c_str()[0]) != OPERATION.end())
        {
            if (operations.empty())
            {
                operations.push_back(arr[i]);
            }
            else if (arr[i].compare(")") == 0)
            {
                while (true)
                {
                    string current = operations[operations.size() - 1];
                    operations.pop_back();
                    if (current.compare("(") == 0)
                    { 
                        break;
                    }
                    result.push_back(current);
                }
            }
            else if (priority(operations[operations.size() - 1]) <= priority(arr[i]))
            {
                operations.push_back(arr[i]);
            }
            else
            {
                while (true)
                {
                    if (operations.empty())
                    {
                        break;
                    }

                    string current = operations[operations.size() - 1];
                    if (priority(current) <= priority(arr[i]))
                    {
                        break;
                    }
                    result.push_back(current);
                    operations.pop_back();
                }
                operations.push_back(arr[i]);
            }
        }
        else
        {
            result.push_back(arr[i]);
        }
    }

    while (!operations.empty())
    {
        string current = operations[operations.size() - 1];
        result.push_back(current);
        operations.pop_back();
    }

    return result;
}

vector<int> simple_calculate(vector<int> A, vector<int> B, string op)
{
    vector<int> result;
    if (op.compare("-") == 0)
    {
        for (int i = 0; i < A.size(); i++)
        {
            if (A[i] <= B[i])
            {
                result.push_back(1);
            }
            else
            {
                result.push_back(0);
            }
        }
    }
    else if (op.compare("-") == 0)
    {
        for (int i = 0; i < A.size(); i++)
        {
            if (A[i] <= B[i])
            {
                result.push_back(1);
            }
            else
            {
                result.push_back(0);
            }
        }
    }
    else if (op.compare("&") == 0) {
        for (int i = 0; i < A.size(); i++)
        {
            if (A[i] == B[i] && A[i] != 0)
            {
                result.push_back(1);
            }
            else {
                result.push_back(0);
            }
        }
    }
    else if (op.compare("|") == 0)
    {
        for (int i = 0; i < A.size(); i++)
        {
            if (A[i] == 1 || B[i] == 1)
            {
                result.push_back(1);
            }
            else
            {
                result.push_back(0);
            }
        }
    }

    return result;
}


vector<int> calculate_result_table(vector<string> expression)
{
    vector<string> arr = rpn(expression);
    vector<vector<int>> table = parse_expression(expression).second;
    stack<vector<int>> stack;

    for (int i = 0; i < arr.size(); i++)
    {
        if (isDigit(arr[i])) 
        {
            stack.push(table[stoi(arr[i])]);
        }
        else if (arr[i].compare("!") == 0)
        {
            vector<int> a1 = stack.top();
            stack.pop();
            stack.push(negat(a1));
        }
        else
        {
            vector<int> a2 = stack.top();
            stack.pop();
            vector<int> a1 = stack.top();
            stack.pop();
            stack.push(simple_calculate(a1, a2, arr[i]));
        }
    }

    try 
    {
        return stack.top();
    }
    catch (exception ex) 
    {
        vector<int> single = { 0 };
        return single;
    }
}




void print_answer(vector<string> expression) 
{
    vector<int> result = calculate_result_table(expression);
    int zero_count = 0;
    int unit_count = 0;
    for (int integer : result) {
        if (integer == 0) zero_count++;
        else if (integer == 1) unit_count++;
    }

    if (zero_count == 0) {
        cout<<"Valid";
    }
    else if (unit_count == 0) {
        cout << "Unsatisfiable";
    }
    else {
        printf("Satisfiable and invalid, %d true and %d false cases", unit_count, zero_count);
    }
}

void replace_all(
    std::string& s,
    std::string const& toReplace,
    std::string const& replaceWith
) 
{
    std::string buf;
    std::size_t pos = 0;
    std::size_t prevPos;

    // Reserves rough estimate of final size of string.
    buf.reserve(s.size());

    while (true) {
        prevPos = pos;
        pos = s.find(toReplace, pos);
        if (pos == std::string::npos)
            break;
        buf.append(s, prevPos, pos - prevPos);
        buf += replaceWith;
        pos += toReplace.size();
    }

    buf.append(s, prevPos, s.size() - prevPos);
    s.swap(buf);
}


int main() {
    std::string s;
    getline(std::cin, s);

   
    replace(s.begin(), s.end(), ' ', '\0');
    replace_all(s, "!!", "");
    replace(s.begin(), s.end(), '\t', '\0');
    replace(s.begin(), s.end(), '\r', '\0');
    vector<string> str;
    string temp = "";
    for (int i = 0; i < s.size(); i++) {
        
        if (s[i] == ' ') {
            str.push_back(temp);
            temp = "";
        }
        else {
            temp += s[i];
        }
    }
    str.push_back(temp);
    print_answer(str);
    getchar();
}