#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node = malloc(sizeof(listint_t));
    listint_t *current_node = *head;
    listint_t *prev_node = NULL;

    if (!new_node)
        return NULL;

    new_node->n = number;
    new_node->next = NULL;

    if (!*head)
        *head = new_node;
    else if (current_node->n > number)
    {
        new_node->next = current_node;
        *head = new_node;
    }
    else
    {
        while (current_node && current_node->n < number)
        {
            prev_node = current_node;
            current_node = current_node->next;
        }

        new_node->next = current_node;
        prev_node->next = new_node;
    }

    return new_node;
}

int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 10);
    add_nodeint_end(&head, 20);
    add_nodeint_end(&head, 30);
    add_nodeint_end(&head, 40);

    printf("Original list:\n");
    print_listint(head);

    insert_node(&head, 27);

    printf("List after adding new node:\n");
    print_listint(head);

    free_listint(head);

    return (0);
}
