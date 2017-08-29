#include <string.h>
#include <stdio.h>

class CA{
    public:
        void eat(int a = 3)
        {
            printf("CA eat,");
            printf("%d,",a);
        }
};

class CB:public CA{
    public:
        void eat(int a = 4)
        {
            printf("CB eat,");
            printf("%d,",a);
        }
};

int main()
{
    CA *a = new CB();
    a->eat();

    CB *b = new CB();
    b->eat();

    return 0;
}
