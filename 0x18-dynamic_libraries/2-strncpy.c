#include "main.h"
#include <string.h>
/**
 * _strncpy - Function that copies a string.
 *
 * @dest: first pointer to be changed
 * @src: second pointer to be changed
 * @n: value
 *
 * Return: always dest
 */

char *_strncpy(char *dest, char *src, int n)
{
        int i;

        i = 0;
        while (i < n && src[i] != '\0')
        {
                dest[i] = src[i];
                i++;
        }
        while (i < n)
        {
                dest[i] = '\0';
                i++;
        }
        return (dest);
}
