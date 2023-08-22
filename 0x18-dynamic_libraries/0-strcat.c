#include "main.h"
#include <string.h>
/**
 * _strcat - function that concatenates two strings src and dest
 *
 * @dest: first pointer to the string
 * @src: second pointer to the string
 *
 * Return: pointer to destination string
 */

char *_strcat(char *dest, char *src)
{
        int length, j;

        length = 0;
        while (dest[length] != '\0')
        {
                length++;
        }
        for (j = 0; src[j] != '\0'; j++, length++)
        {
                dest[length] = src[j];
        }
                dest[length] = '\0';

        return (dest);
}
