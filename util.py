# The functions in this file are to be implemented by students.

import bitio
import huffman


def read_tree(bitreader):
    '''Read a description of a Huffman tree from the given bit reader,
    and construct and return the tree. When this function returns, the
    bit reader should be ready to read the next bit immediately
    following the tree description.

    Huffman trees are stored in the following format:
      * TreeLeaf is represented by the two bits 01, followed by 8 bits
          for the symbol at that leaf.
      * TreeLeaf that is None (the special "end of message" character)
          is represented by the two bits 00.
      * TreeBranch is represented by the single bit 1, followed by a
          description of the left subtree and then the right subtree.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.

    Returns:
      A Huffman tree constructed according to the given description.
    '''
    bit = bitreader.readbit()

    if bit == 1: # if first bit is one it's a branch
        # recursively call self to make branch i guess
        left = read_tree(bitreader)
        right = read_tree(bitreader)

        # return branch that is found probably
        # like return branch with its left and right leaves
        return huffman.TreeBranch(left, right)

    if bit == 0:
        # if first bit is 0 it is a leaf i think
        bit = bitreader.readbit()

        if bit == 1: # tree leaf with value "01"
            return huffman.TreeLeaf(bitreader.readbits(8))
        elif bit == 0: # tree leaf with value "00"
            return huffman.TreeLeaf(None)
            # return huffman.TreeLeafEndMessage() # NEED TO DO SOMETHING HERE I THINK

def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leave is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    while True:
        bit = bitreader.readbit()
        # Check if the node is the EOF is reached, return nothing and stop decoding

        # THIS LINE IS BROKEN IDK HOW TO FIX SOS
        # if isinstance(tree, None): # NOT SURE IF THIS FIXES A PROBLEM TreeLeafEndMessage):
            # return None
        # Check if the node is a Leaf node, return the value of this node
        # if isinstance(tree, TreeLeaf):
        #     # if tree.value == None:
        #     #     return None
        #     # else:
        #     return tree.value
        # If niether then must be a Branch, check the current bit to see where to go
        # else:
            # 0 bit means move toward left branch based on Huffman Tree
            if bit == 0:
                tree = tree.left
            # Bit == 1, move towards right branch based on Huffman Tree
            else:
                tree == tree.right

        # This probably doesn't fix anything but at least i tried i guess
        if isinstance(tree, TreeLeaf):
            return tree.value

        # elif tree is not None:
        #     if bit == 0:
        #         tree = tree.left
        #     else:
        #         tree == tree.right
        #
        # else:
        #     return None


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''
    # Gets bits from compressed file stream
    #bitio.BitReader object wrapping the compressed stream to be able to read the input one bit at a time
    bitInputStream = bitio.BitReader(compressed)

    # construct BitWriter object for 'unompressed' file stream
    bitwriter = bitio.BitWriter(uncompressed)

    # read huffman tree from the compressed file using read_tree
    tree = read_tree(bitInputStream)

    # Repeatedly read coded bits from the file, decode them using tree
    while True:
        decodedBytes = decode_byte(tree, bitInputStream)

        # if found end of message, stop reading
        if decodedBytes == None:
            break
        # Write the stored values in the tree (ordered by bit sequence)
        # else:
        #     uncompressed.write(bytes([decodedBytes]))  # as a byte in uncompressed
        bitwriter.writebits(decodedBytes, 8)




def write_tree(tree, bitwriter):
    '''Write the specified Huffman tree to the given bit writer.  The
    tree is written in the format described above for the read_tree
    function.

    DO NOT flush the bit writer after writing the tree.

    Args:
      tree: A Huffman tree.
      bitwriter: An instance of bitio.BitWriter to write the tree to.
    '''
    pass


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''
    pass
