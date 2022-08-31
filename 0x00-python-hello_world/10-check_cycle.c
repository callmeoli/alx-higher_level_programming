#include <stdio.h>
#include "lists.h"
/**
* check_cycle - check whether there is cycle or not
* @list: head of the linked list
* Return: 0 if there is no cycle 1 if there is cycle
*/
int check_cycle(listint_t *list)
{
listint_t *slow;
listint_t *fast;
slow = list;
fast = list;


while (fast->next->next != NULL)
{
	slow = slow->next;
	fast = fast->next->next;
	if (slow == fast)
	{
		return (1);
	}
}
return (0);
}
