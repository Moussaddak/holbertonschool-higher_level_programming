#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is a palindrome.
 *@head: input singly list
 *Return: (1):palindrome / (0): not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head, *first, *last;
	int i, j, k, n = 0;

	if (!&head)
	{
		return (1);
	}
	while (node)
	{
		node = node->next;
		n++;
	}
	for (i = 0; i < n / 2; i++)
	{
		first = *head;
		last = *head;
		for (j = 0; j < i; j++)
		{
			first = first->next;
		}
		for (k = 0; k < n - 1 - i; k++)
		{
			last = last->next;
		}
		if (first->n == last->n)
		{
			return (1);
		}
	}
	return (0);
}
