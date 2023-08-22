#include "main.h"

/**
 * _puts - prints a stand out string
 *
 * @str: pointer to the string to print
 *
 * Return: void
 */

void _puts(char *str)
{
        int j;

        while (j >= 0)
        {
                if (str[j] == '\0')
                {
                _putchar (str[j]);
                        j++;
                }
                        _putchar ('\n');
        }
}
