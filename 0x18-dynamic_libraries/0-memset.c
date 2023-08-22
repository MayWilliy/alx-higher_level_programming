#include "main.h"

/**
 * _memset - fills the first n byte memory area pointed by s with cons b
 *
 * @n: number of byte to fill
 * @s: pointer to the memory byte area to fill
 * @b: constant byte to fill by the memeory
 *
 * Return: pointer to the memory area of s
 */

char *_memset(char *s, char b, unsigned int n)
{
        unsigned int i;

        for (i = 0; i < n; i++)
        {
                s[i] = b;
        }
        return (s);
}	
