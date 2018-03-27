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

Functionality implemented:
- [x] Theutil.write_treefunctiontowriteHuffmantreesintofilesintheformatdescribedbelow (step 3 above).
- [x] The util.compress function to accomplish steps 3 and 4 above (using util.write_tree for step 3).
- [x] The util.decode_byte function that will return a single byte representing the next character of the original text that is encoded in the BitReader corresponding to the compressed text.
- [x] The util.read_tree function to read Huffman trees from files (step 5 above)
- [x] Theutil.decompressfunctiontoaccomplishsteps5and6above(usingutil.read_tree for step 5).

## HOW TO RUN:

Running the Web Server

- Once you have implemented the `decompress` function, you will be able to run the webserver.py script to serve compressed files. To try this out, change to the `wwwroot/` directory included with the assignment and run
```
python3 ../webserver.py
```
- Then open the url http://localhost:8000 in your web browser. If all goes well, you should see a web page including an image. Compressed versions of the web page and the image are stored as `index.html.huf` and `huffman.bmp.huf` in the `wwwroot/` directory. The web server is using your decompress function to decompress these files and serve them to your web browser.

Running the Compressor

- Once you have implemented the `util.compress` function, you will be able to run the `compress.py` script to compress files. For example, to add a new file `[filename].pdf` to be served by the web server, copy it to the `wwwroot/` directory, change to that directory, and run
```
python3 ../compress.py somefile.pdf
```
- This will generate somefile.pdf.huf and you will be able to access the decompressed version at the URL http://localhost:8000/somefile.pdf. You should download the decompressed file and compare it to the original using the `cmp` command, to make sure there are no differences.
