# Huffman Coding

Program that compresses and decompresses files using Huffman codes. The compressor will be a command-line utility that encodes any file into a compressed version with a .huf extension. The decompressor will be a web server that will let you directly browse com- pressed files, decoding them on-the-fly as they are being sent to a web browser.

To encode a messages using Huffman codes requires the following steps:

1. Read through the message and construct a frequency table counting how many times each symbol (i.e. byte in our case) occurs in the input (huffman.make_freq_table does this).
2. Construct a Huffman tree (called tree) using the frequency table (huffman.make_tree does this).
3. Write tree to the output file, so that the recipient of the message knows how to decode it (you will write the code to do this in util.write_tree).
4. Read each byte from the uncompressed input file, encode it using tree, and write the code sequence of bits to the compressed output file. The function huffman.make_encoding_table takes tree and produces a dictionary mapping bytes to bit sequences; constructing this dictionary once before you start coding the message will make your task much easier,

Decoding a message produced in this way requires the following steps:

5. Read the description of tree from the compressed file, thus reconstructing the original Huffman tree that was used to encode the message (you will write the code to do this in util.read_tree).
6. Repeatedly read coded bits from the file, decode them using tree (the util.decode_byte function does this), and write the decoded byte to the uncompressed output.

You will implement the following functionality:
- [ ] Theutil.write_treefunctiontowriteHuffmantreesintofilesintheformatdescribedbelow (step 3 above).
- [ ] The util.compress function to accomplish steps 3 and 4 above (using util.write_tree for step 3).
- [ ] The util.decode_byte function that will return a single byte representing the next character of the original text that is encoded in the BitReader corresponding to the compressed text.
- [ ] The util.read_tree function to read Huffman trees from files (step 5 above)
- [ ] Theutil.decompressfunctiontoaccomplishsteps5and6above(usingutil.read_tree for step 5).
