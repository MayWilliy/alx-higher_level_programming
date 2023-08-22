#include "main.h"

/**
 * _memcpy - cop n byte from memory area src to dest
 *
 * @n: number of memory btye to copy
 * @src: pointer to source memory
 * @dest: pointer to destination memory
 *
 * Return: pointer to destination
 */

char *_memcpy(char *dest, char *src, unsigned int n)
{
        char *magicstick1 = src;
        char *magicstick2 = dest;

        while (n)
        {
                *(magicstick2++) = *(magicstick1++);
                n--;
        }
        return (dest);
}
