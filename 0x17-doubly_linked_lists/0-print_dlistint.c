#include <stdio.h>
#include "lists.h"
/**
* print_dlistint -print content form liked list
* @h: header
* Return: size of linked list
*/
size_t print_dlistint(const dlistint_t *h)
{
dlistint_t *current;
int count = 0;

current = (dlistint_t *)h;
while (current != NULL)
{
	printf("%d\n", current->n);
	current = current->next;
	count++;
}
return (count);
}
