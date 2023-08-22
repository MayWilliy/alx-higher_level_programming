#include "main.h"
#include <string.h>

/**
 * _strcmp - function that compares two strings
 *
 * @s1: first pointer to string
 * @s2: second poniter to string
 *
 * Return: value less than 0 if string  is less than the other
 * Value greater than 0 if string is greater than the other
 * 0 if string is equal
 */

int _strcmp(char *s1, char *s2)
{
        int counter, comVal;

        counter = 0;
        while (s1[counter] == s2[counter] && s1[counter] != '\0')
        {
                counter++;
        }
        comVal = s1[counter] - s2[counter];
        return (comVal);
}
