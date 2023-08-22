#include "main.h"

/**
 * *_isupper - check if a character is uppercase
 *
 *      * @c: parameter
 *
 *      *Return: 0 if successful
 */
int _isupper(int c)
{
        if (c >= 'A' && c <= 'Z')
        {
                return (1);
	}
        else
        {
                return (0);
	}
}
