/* testcode1.c
 * Write CSV file which includes tim
 *
 */

#include <stdio.h>
#include <sys/time.h>

int main(int argc, const char**  argv)
{
    struct timeval tv;
    gettimeofday(&tv,NULL);
    printf("seconds %ld microseconds %ld\n", tv.tv_sec, tv.tv_usec);
    return 0;
}
