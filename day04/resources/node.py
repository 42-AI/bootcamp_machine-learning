class Node:
    def __init__(self, data=None, labels=None,
                 is_leaf=False, split_feature=None, split_kind=None, split_criteria=None,
                 left=None, right=None,
                 depth=0):
        """
        :param pandas.Dataframe data: features
        :param pandas.Dataframe labels: labels

        :param bool is_leaf: True if the node is a leaf of the tree
        :param int split_feature: column of the feature
        :param str split_kind: ["<=" or "="]
        :param split_criteria: value of the criteria used to split data

        :param Node left: node child where criteria is True
        :param Node right: node child where criteria is False

        :param int depth: depth level of the node in the tree
        """
        # data
        self.X = data
        self.y = labels

        # split_info
        self.is_leaf = is_leaf
        self.split_feature = split_feature
        self.split_kind = split_kind
        self.split_criteria = split_criteria
        if self.is_leaf:
            self.content = "Leaf"
        else:
            self.content = "Feature {} {} {}".format(self.split_feature, self.split_kind, self.split_criteria)

        # children
        self.left_child = left
        self.right_child = right

        # meta
        self.depth = depth

    def __str__(self):
        output_print = """{}\nNode depth = {}\n\n""".format(self.content, self.depth)
        if self.is_leaf:
            output_print += """X =\n{}\n\ny = \n{}\n""".format(self.X, self.y)
        return output_print
