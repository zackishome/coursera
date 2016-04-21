#ifndef GENERICS_H
#define GENERICS_H

typedef int (*cmp_t)(void *, void *);

extern void *max(void **p,int num, cmp_t cmp);

#endif