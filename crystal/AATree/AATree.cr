class AANode 
    property :value, :parent, :left, :right, :level

    def initialize(value : Int32, level : Int32, left : (AANode | Nil)=nil, right : (AANode | Nil)=nil, parent : (AANode | Nil)=nil)
        @value = value
        @level = level
        @parent = parent
        @left = left
        @right = right
    end
end
struct Nil
    # TODO: Remove this hack
    def parent
        raise "WTF"
    end

    def parent=(tk)
        raise "WTF"
    end
    
    def right
        raise "WTF"
    end
    def right=(tk)
        raise "WTF"
    end
    def level
        raise "WTF"
    end
    def level=(tk)
        raise "WTF"
    end
    def is_right_grandchild?(grandparent : AANode)
        raise "WTF"
    end
end
class AATree
    def initialize(root : AANode)
        @root = root
        @count = 1
    end
end

class AANode
    #
    # Returns the grandparent of the node
    #
    def grandparent : (AANode | Nil)
        if @parent.nil?
            nil
        else
            @parent.parent
        end
    end

    #
    # Returns a boolean indicating if the given aaNode is the right grandchild
    # 1								5
    #  \								 \
    #   2								  7
    #    \							 /
    #     3 							6
    #  In the above example, 3 is a right grandchild of 1.
    #  6 is not a right grandchild of 5
    #
    def is_right_grandchild?(grandparent : AANode)
        (!grandparent.right.nil?) && (!grandparent.right.right.nil?) && grandparent.right.right == self
    end
end

class AATree
    def initialize(root : AANode)
        @root = root
        @count = 1
    end
    #
    # Adds a value into the tree
    #
    def add(value : Int32)
        if @root.nil?
            # TODO:
        else
            self._add(value, @root)
        end
        @count += 1
    end

    #
    # The internal add function, which traverses the trees nodes until it lands at the correct node,
    # left/right of which the new node should be inserted.
    # Backtracing from the recursion, we check if we should perform a split or skew operation*/
    #
    def _add(value : Int32, node : AANode)
        if value < node.value
            # go left
            if node.left.nil?
                # new left AANode
                new_node = AANode.new(value: value, level: 1, parent: node)
                node.left = new_node
                check_skew(new_node, true)
            else
                _add(value, node.left.as(AANode))
            end
        elsif value > node.value
            # go right
            if node.right.nil?
                new_node = AANode.new(value: value, level: 1, parent: node)
                node.right = new_node

                # we've added a right node, check for a split
                check_split(new_node)
            else
                _add(value, node.right.as(AANode))
            end
        else
            raise Exception.new("Equal elements are unsupported!")
        end

        # backtracing through the path, check for skews and then for splits
        check_skew(node, true)
        check_split(node)
    end

    #
    # Performs a split operation, given the three needed nodes
    # 11(R)                  	12
    #   \			    	   /  \
    #    12(P)   ===>		 11    13
    #     \
    #      13(C)
    #      P becomes the new root, where any leaf that was left of P is now to the right of R
    #      i.e if 12 had a left child 11.5, 11.5 should become the right child of the new 11
    #
    
    def split(grandparent : AANode, parent : AANode)
        # fixes grandparent's link
        grand_grandparent = grandparent.parent
        unless grand_grandparent.nil?
            if grand_grandparent.left == grandparent
                grand_grandparent.left = parent
            else
                grand_grandparent.right = parent
            end
        end 

        if grandparent == @root
            # we now have a new root
            @root = parent
        end

        parent.parent = grand_grandparent  # R parent is now some upwards node
        grandparent.parent = parent  # R parent is now P
        grandparent.right = parent.left
        unless parent.left.nil?
            parent.left.parent = grandparent
        end
        parent.left = grandparent
        parent.level += 1
    end

    # Given a node, check if a Split operation should be performed, by checking the node's grandparent level
	# The node we're given would be the downmost one in the split operation */
    def check_split(node : AANode)
        grandparent = node.grandparent
        if (!grandparent.nil?) && node.is_right_grandchild?(grandparent) && grandparent.level <= node.level
            split(grandparent, node.parent.as(AANode))
        end
    end

    #
    # Performs a skew operation, given the two needed nodes
    #     12(A) 1                11(B)1
    #     /          ===>          \
    #   11(B) 1                   12(A)1
    #
    def skew(parent : AANode, leaf : AANode)
        grandparent = parent.parent
        unless grandparent.nil?
            if grandparent.value < parent.value
                # new GP right
                grandparent.right = leaf
            else
                grandparent.left = leaf
            end
        else
            @root = leaf
        end

        leaf.parent = grandparent
        old_right = leaf.right
        leaf.right = parent
        parent.left = old_right
        unless old_right.nil?
            old_right.parent = parent
        end
        parent.parent = leaf
    end

    #  Given a node, check is a Skew operation should be performed by checking if its a left child
    #     and if its level is bigger or equal to his parent's
    # param: checkForSplit - a boolean indicating if we want to split if it's ok to split after the skew
    #         We generally don't want to do that in deletions, as in the example on the TestFunctionalTestTreeRemoval function
    #         where we remove 1 from the tree
    #
    def check_skew(node : AANode, check_for_split : Bool)
        parent = node.parent
        if (!parent.nil?) && parent.left == node && parent.level <= node.level
            skew(parent, node)
            # check for split; Parent would now be the middle element
            if (!parent.right.nil?) && check_for_split
                if parent.right.nil?
                    return
                end
                if parent.right.is_right_grandchild?(node) && node.level <= parent.right.level
                    split(node, parent)
                end
            end
        end
    end
end

root = AANode.new(value: 100, level: 1)
tree = AATree.new(root)

tree.add(101)
tree.add(99)
tree.add(102)
tree.add(103)
tree.add(104)
tree.add(105)
tree.add(130)
tree.add(129)
tree.add(108)
tree.add(109)
