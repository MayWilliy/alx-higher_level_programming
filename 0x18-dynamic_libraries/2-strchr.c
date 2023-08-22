#include "main.h"
#include <stdlib.h>

/**
 * _strchr - function that locates a character in a string
 * @s: pointer to the string
 * @c: pointer to character
 *
 *Return: to c in the string s, or NULL
 */
char *_strchr(char *s, char c)
{
        while (*s != c && *s != '\0')
        {
                s++;

        }

        if (*s == c)
        {
                return (s);
        }
        return (NULL);
}
