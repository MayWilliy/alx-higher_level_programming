#include "main.h"
#include <string.h>
/**
 * _strncat - function that concatenates two strings
 *
 * @dest: first pointer
 * @src: second pointer
 * @n: number of byte to concatenates
 *
 * Return: pointer to designated strings
 */
char *_strncat(char *dest, char *src, int n)
{
        int length, j;

        length = 0;
        while (length[dest] != '\0')
        {
                length++;
        }
        for (j = 0; j < n && src[j] != '\0'; j++, length++)
        {
                dest[length] = src[j];
        }
                dest[length] = '\0';

        return (dest);
}
