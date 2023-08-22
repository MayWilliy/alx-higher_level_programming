#include "main.h"

/**
 * _strlen- returns the length of a string
 *
 * @s: pointer to the string to get lenght of
 *
 * Return: (strlen)
 */

int _strlen(char *s)
{
        int i;

        i = 0;
        while (s[i] != '\0')
                i++;

        return (i);
}
