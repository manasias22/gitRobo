#include <stdio.h>

int main()
{
    char p, commitMessage[100], gitrepo[80];
    system("git init");
    system("git add .");
    printf("The commit message?\n");
    scanf("%[^\n]s",commitMessage);
    system("git commit -m %s", commitMessage);
    // Do you wish to push?
    printf(" Do you wish to push?\nY/N\n");
    scanf("\n%c\n", &p);
    if (p == 'Y' || p == 'y')
    {
        printf("The git repo you wish to push:");
        scanf("%[^\n]s", gitrepo);
        system("git remote add origin %s",gitrepo);
        system("git push -u origin master");
    }
    else{
        exit(0);
    }
    return 0;
}