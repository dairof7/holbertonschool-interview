#include "binary_trees.h"

/**
 * heap_insert - inserts a value into a Max Binary Heap:
 * @root: address of the root or other node
 * @value: value of the new node
 * Description:
 * Este metodo se utiliza cuando queremos ordenar
 * de mayor a menor el arbol. Su complejidad es
 * de orden O(1) para la busqueda y orden O(Log n) para
 * la insercion.
 * Return: a pointer to the new node, or NULL on failure.
 */
heap_t *heap_insert(heap_t **root, int value)
{
	heap_t *current_node = NULL;/* current node */
	int a, b, c, d;

	if (root == NULL)/* si no es nada */
		return (NULL);

	if (*root == NULL)
		return (*root = binary_tree_node(NULL, value));

	current_node = *root;

	while (current_node)
	{
		if (current_node->left == NULL)
		{
			current_node->left = binary_tree_node(current_node, value);
			if (current_node->left == NULL)
				return (NULL);
			return (exchange_order(current_node->left));
		}
		else if (current_node->right == NULL)
		{
			current_node->right = binary_tree_node(current_node, value);
			if (current_node->right == NULL)
				return (NULL);

			return (exchange_order(current_node->right));
		}
		a = binary_tree_is_perfect(current_node->right);
		b = binary_tree_is_perfect(current_node->left);
		c = binary_tree_height(current_node->right);
		d = binary_tree_height(current_node->left);

		if ((a && b && c == d)
			|| (a && !b && c != d))
		current_node = current_node->left;
		else
			current_node = current_node->right;
	}
	return (NULL);
}

/**
 * exchange_order - order some nodes
 * @son: new node
 * Return: returns the current node
 */
heap_t *exchange_order(heap_t *son)
{
	int tmp;
	/* mientras no sea la raiz */
	while (son && son->parent)
	{
		/* si ya esta ordenado */
		if (son->n < son->parent->n)
			return (son);
		tmp = son->n;
		/* el hijo obtiene el valor del padre */
		son->n = son->parent->n;
		/* el padre obtiene el valor del hijo */
		son->parent->n = tmp;
		/* cambiar el foco al nodo padre */
		son = son->parent;
	}
	return (son);
}

/**
 * binary_tree_height - measures the height of a binary tree.
 * Description: height is the distance from the chosen node
 * to the most distant child node. So the distance between
 * a node and its first child would be 1.
 * @tree: a pointer to the root node of the
 * tree to measure the height.
 *
 * Return: height | 0
 */
size_t binary_tree_height(const binary_tree_t *tree)
{
	size_t h_left, h_right;

	if (tree == NULL)
		return (0);

	if (tree->left)
		h_left = 1 + binary_tree_height(tree->left);
	else
		h_left = 0;

	h_right = tree->right ? 1 + binary_tree_height(tree->right) : 0;

	if (h_left > h_right)
		return (h_left);
	else
		return (h_right);
}

/**
 * binary_tree_is_perfect - checks if a binary tree is perfect.
 * Description: it's perfect when you have all your sheets
 * at the same level.
 * @tree: a pointer to the root node of the tree to check.
 *
 * Return: 1 | 0
 */
int binary_tree_is_perfect(const binary_tree_t *tree)
{
	int s, h, max_n;

	if (tree == NULL)
		return (0);

	s = binary_tree_size(tree);
	h = binary_tree_height(tree);

	/*
	* maximum number of nodes with height.
	* (2 << h) - 1 == (2 * 2^h) - 1
	*/
	max_n = (2 << h) - 1;

	return (s == max_n);
}

/**
 * binary_tree_size - measures the size of a binary tree.
 * Description: the size is a number of all(direct and indirect)
 * child nodes including the parent node.
 * @tree: a pointer to the root node of the tree to measure the size
 *
 * Return: size | 0
 */
size_t binary_tree_size(const binary_tree_t *tree)
{
	if (tree != NULL)
	{
		return (
		1 +
		binary_tree_size(tree->left) +
		binary_tree_size(tree->right)
		);
	}
	else
	{
		return (0);
	}

}
