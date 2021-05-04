#include "lists.h"
/**
 * listint_len - function that returns the number of elements
 * in a linked listint_t list.
 * @h: take a list type of listint_t
 * Return: number of elements of @h list
 **/
size_t listint_len(const listint_t *h)
{
	size_t s = 0;

	if (h == NULL)
		return (0);
	while (h)
	{
		s++;
		h = h->next;
	}

	return (s);
}
/**
 * is_palindrome - function in C that checks if a singly linked list is
 * a palindrome.
 * @head: pointer to head of a listint_t
 * Return: 0 if it is not palindrome otherwise 1
 **/
int is_palindrome(listint_t **head)
{
	size_t len;
	unsigned int i = 0;
	listint_t *tmp;
	int list[2048];

	tmp = *head;
	len = listint_len(tmp);
	if (len == 0)
		return (1);
	while (tmp)
	{
		list[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	for (i = 0; i < len; i++)
	{
		if (list[i] != list[len - i - 1])
			return (0);
	}
	return (1);
}
