#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: linked list to check
 *
 * Return: 0 if there is no cycle, and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cur = list;
	listint_t *head = list;

	while (head != NULL && head->next != NULL)
	{
		cur = cur->next;
		head = head->next->next;
		if (cur == head)
			return 1;
	}

	return 0;
}
