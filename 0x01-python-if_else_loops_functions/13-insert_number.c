#include "lists.h"

/**
 * insert_node - Inserts into a sorted singly-linked list a number.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *n;

	m = malloc(sizeof(listint_t));
	if (n == NULL)
		return (NULL);
	n->m = number;

	if (node == NULL || node->m >= number)
	{
		n->next = node;
		*head = n;
		return (n);
	}

	while (node && node->next && node->next->m < number)
		node = node->next;

	n->next = node->next;
	node->next = n;

	return (n);
}
