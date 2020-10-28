                                                                                                   newtime.c                                                                                                               
#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

// Name: Jason Cariaga
// netID: jmc803
// RUID: 171001720
// your code for time() goes here
#include <time.h>
#include <dlfcn.h>

int state = 1;

time_t time(time_t *tloc){
        //declare time fcn pointer
        time_t (*new_time)(time_t *tloc);
        //pt1 code here:
        struct tm tm;
        strptime("2020 April 20 12:00:00", "%Y %b %d %H:%M:%S", &tm);
        time_t temp = *tloc; //works to get a copy of tloc state
        *tloc = mktime(&tm);

        //calls real time function
        new_time = dlsym(RTLD_NEXT, "time");

        //time_t temp = time(tloc);
        return *tloc;
        //return temp;
}


