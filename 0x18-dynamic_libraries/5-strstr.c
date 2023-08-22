#include "main.h"

/**
 * _strstr - function that locates a substring
 * @haystack: the string to search in
 * @needle: the string to search for
 *
 * Return: a pointer to the beginning of the located substring or NULL
 */

char *_strstr(char *haystack, char *needle)
{
        int i, j, k;

        for (i = 0; haystack[i] != '\0'; i++)
        {
                for (j = i, k = 0; needle[k] != '\0' && haystack[j] == needle[k]; j++, k++)
                        ;
                        if (needle[k] == '\0')
                                return (haystack);
        }
                return ('\0');
}
