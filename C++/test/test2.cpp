#include <string.h>
#include <stdio.h>

class CA{
    public:
        virtual void eat(int a = 3)
        {
            printf("CA eat,");
            printf("%d,",a);
        }
};

class CB:public CA{
    public:
        virtual void eat(int a = 4)
        {
            printf("CB eat,");
            printf("%d,",a);
        }
};

int main()
{
    CB b;
    b.eat();

    CA a = b;
    a.eat();

    return 0;
}
