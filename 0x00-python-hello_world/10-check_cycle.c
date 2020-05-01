#include "lists.h"
/**
 * check_cycle - check if single linked is cyclic
 * @list: list to check
 * Return: 1 if loop detected 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *step_1 = list, *step_2 = list;

	if (!list)
		return (0);

	while (step_2 && step_2->next && step_2->next->next)
	{
		step_1 = step_1->next;
		step_2 = step_2->next->next;

		if (step_1 == step_2)
			return (1);
	}
	return (0);
}
