#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string word;
    cin >> word;

    int with_y = 0;
    int without_y = 0;

    for (char a : word)
    {
        if (a == 'a' || a == 'e' || a == 'i' || a == 'o' || a == 'u')
        {
            without_y++;
            with_y++;
        }
        else if (a == 'y')
        {
            with_y++;
        }
    }

    cout << without_y << " " << with_y << endl;
}
