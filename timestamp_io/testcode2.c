/*
 * The functions gmtime and localtime (for UTC and local time respectively) will turn an arbitrary time_t into a struct tm. 
 */
#include <stdio.h>
#include <time.h>

int main(int argc, const char** argv)
{
    int i;
    time_t ltime;
    char buff[20];
 
    ltime = time(NULL);
    strftime(buff, 20, "%Y-%m-%d %H:%M:%S", localtime(&ltime));
    printf("localtime=%s\n", buff);

    time(&ltime);
    printf ("Coordinated Universal Time: asctime= %s", asctime(gmtime(&ltime)));
    for(i=0; i< 10; i++){
        ltime = ltime + 10;
        printf ("[%d] asctime(gmtime)=%s", i, asctime(gmtime(&ltime)));
        strftime(buff, 20, "%Y-%m-%d %H:%M:%S", localtime(&ltime));
        printf("[%d] strftime(localtime)=%s\n", i, buff);
        strftime(buff, 20, "%Y-%m-%d %H:%M:%S", gmtime(&ltime));
        printf("[%d] strftime(gmtime)=%s\n", i, buff);
    }

    FILE* f;
    f = fopen("timestamp.csv", "w");
    fprintf(f, "datetime,val1,val2\n");
    for(i=0; i< 10; i++){
        ltime = ltime + 10;
        strftime(buff, 20, "%Y-%m-%d %H:%M:%S", gmtime(&ltime));
        fprintf(f, "%s.%06d,%lf,%lf\n", buff, (i%10)*100*1000, 123.456*i, -10.0*i);
    }
    fclose(f);
    return 0;
}