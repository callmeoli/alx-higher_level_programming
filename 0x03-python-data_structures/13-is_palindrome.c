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
int k;
int i = 0;
int j = 0;

current = *head;
end = *head;

while (end->next != NULL)
{
	end = end->next;
	count++;
}
end = *head;
k = count;

while (i != k / 2)
{
while (j < count) // we got to the end @count
{
	end = end->next;
	j++;
}
count--;
j = 0;
if (end->n != current->n) // we compare end with current 
	return (0);
current = current->next; //we got to the next current
i++;
end = *head;
}
return (1);
}
