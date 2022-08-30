#include <stdio.h>
#include "lists.h"
/**
* is_palindrome - check whethere list is palindrome
* @head: head of list
* Return: int
*/
int is_palindrome(listint_t **head)
{
listint_t *current;
listint_t *end;
int count = 0;

current = *head;
end = *head;

while (end->next != NULL)
{
	end = end->next;
	count++;
}
if (end->n != current->n)
	return (0);
else
	return (1);
}