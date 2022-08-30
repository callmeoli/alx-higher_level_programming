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
int i = 0;


current = *head;
end = *head;
if (*head == NULL)
{
	return (1);
}
while (end->next != NULL)
{
	end = end->next;
	count++;
}
end = *head;

while (i != count / 2)
{
int j = 0;

while (j < (count - i))
{
	end = end->next;
	j++;
}
j = 0;
if (end->n != current->n)
	return (0);
current = current->next;
i++;
end = *head;
}
return (1);
}
